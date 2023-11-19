from flask import Flask, render_template, Response
import cv2
from cvzone.PoseModule import PoseDetector
import time
import math

app = Flask(__name__, static_url_path='',
                  static_folder='build',
                  template_folder='build')

detector = PoseDetector()
capture = cv2.VideoCapture(0)

targetLimbs = []
deltaTime = 0.0
counter = 5.0
gameState = 0
didWin = "Congratulations"
accuracy = 0
screenX = 1
screenY = 1

minHandDistance = 50
rightHandPos = [0, 0]
leftHandPos = [0, 0]

rightBarPos = [0,0]
leftBarPos = [0,0]

nextHandVel = -1.0
handVelocity = 0.0

prevRightHandPos = [0,0]
prevLeftHandPos = [0,0]
handLineOffset = 0.0
def handsTogether() -> bool:
    dist = math.sqrt((rightHandPos[0] - leftHandPos[0])**2 + (rightHandPos[1] - leftHandPos[1])**2)
    return dist < minHandDistance
def distance(bar_positions, hand_positions):
    distance_left = math.sqrt((bar_positions[0][0] - hand_positions[0][0])**2 + (bar_positions[0][1] - hand_positions[0][1])**2)
    distance_right = math.sqrt((bar_positions[1][0] - hand_positions[1][0]) ** 2 + (bar_positions[1][1] - hand_positions[1][1]) ** 2)
    if distance_left >= 40 or distance_right >= 40:
        return False
    return True

def drawHandLine(img):
    global handLineOffset
    global deltaTime
    global accuracy
    global screenY
    handLineOffset += 23.0 * (deltaTime*25)
    if (handLineOffset > 360):
        handLineOffset = 0
    pos = int(math.cos(math.radians(handLineOffset)) * 15)
    barY = 250 + pos
    rightBarPos[0] = screenX - 100
    rightBarPos[1] = barY
    leftBarPos[0] = screenX + 100
    leftBarPos[1] = barY
    barColor = (255,255,255)
    if distance((leftBarPos, rightBarPos), (rightHandPos, leftHandPos)):
        barColor = (61,235,69)
        accuracy +=1 * deltaTime
        print(accuracy)
    else:
        barColor = (0, 0, 255)

    cv2.line(img, (screenX - 100, barY), (screenX + 100, barY), barColor, 2)
    cv2.circle(img, (int(leftBarPos[0]), int(leftBarPos[1])), 10, barColor, -1)
    cv2.circle(img, (int(rightBarPos[0]), int(rightBarPos[1])), 10, barColor, -1)

#cv2.namedWindow('Frame', cv2.WINDOW_NORMAL)

def generate_frames():
    global gameState, counter, deltaTime, screenX, accuracy, didWin, nextHandVel
    while True:
        currentTime = time.time()
        success, img = capture.read()
        if not success:
            continue

        img = detector.findPose(img, True)
        print(screenX)
        lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False)
        if (gameState != 0):
            if (counter > 0):
                counter -= 1 * deltaTime
                if (counter < 0):
                    counter = 10
                    gameState += 1
                    if (gameState > 3):
                        gameState = 0
                        counter = 0
                        accuracy = 0.0

            if (gameState == 1):
                cv2.putText(img, 'GET INTO POSITION', (27, 30), cv2.FONT_HERSHEY_PLAIN, 2, (52, 192, 235), 2,
                            cv2.LINE_AA)
                cv2.putText(img, str(int(counter)), (165, 70), cv2.FONT_HERSHEY_PLAIN, 3, (52, 192, 235), 2,
                            cv2.LINE_AA)
            if gameState == 2:
                cv2.putText(img, 'START COMPRESSIONS', (27, 30), cv2.FONT_HERSHEY_PLAIN, 2, (52, 192, 235), 2,
                            cv2.LINE_AA)
                cv2.putText(img, str(int(counter)), (165, 70), cv2.FONT_HERSHEY_PLAIN, 3, (52, 192, 235), 2,
                            cv2.LINE_AA)
            if gameState == 3:
                if accuracy < 6.5:
                    didWin = "Try Again :/"
                elif 6.5 < accuracy:
                    didWin = "Congratulations!"
                cv2.putText(img, f"{didWin}", (27, 30), cv2.FONT_HERSHEY_PLAIN, 2, (52, 192, 235), 2, cv2.LINE_AA)
                cv2.putText(img, f"Your Accuracy Was: {int(accuracy * 10)}%", (27, 60), cv2.FONT_HERSHEY_PLAIN, 2,
                            (52, 192, 235), 2, cv2.LINE_AA)
        else:
            cv2.putText(img, f"Press 'SPACE' to Start", (27, 30), cv2.FONT_HERSHEY_PLAIN, 2, (52, 192, 235), 2,
                        cv2.LINE_AA)
        if lmList:
            right_shoulder = lmList[12]
            left_shoulder = lmList[11]

            right_hip = lmList[24]
            left_hip = lmList[23]
            lmList[23] = [30, 20, 20]

            leftHandPos = [(lmList[16][0] + lmList[18][0] + lmList[20][0] + lmList[22][0]) / 4,
                           (lmList[16][1] + lmList[18][1] + lmList[20][1] + lmList[22][1]) / 4]
            rightHandPos = [(lmList[15][0] + lmList[17][0] + lmList[19][0] + lmList[21][0]) / 4,
                            (lmList[15][1] + lmList[17][1] + lmList[19][1] + lmList[21][1]) / 4]

            handsColor = (0, 0, 0)

            if (handsTogether()):
                handsColor = (102, 255, 51)
            else:
                handsColor = (0, 0, 255)

            if (time.time() > nextHandVel):
                nextHandVel = time.time() + 0.5

            cv2.circle(img, (int(leftHandPos[0]), int(leftHandPos[1])), 10, handsColor, -1)
            cv2.circle(img, (int(rightHandPos[0]), int(rightHandPos[1])), 10, handsColor, -1)

            shoulder_distance = math.sqrt((right_shoulder[0] - left_shoulder[0]) ** 2 +
                                          (right_shoulder[1] - left_shoulder[1]) ** 2)

            hip_distance = math.sqrt((right_hip[0] - left_hip[0]) ** 2 +
                                     (right_hip[1] - left_hip[1]) ** 2)

            shoulder_mid_x = int((right_shoulder[0] + left_shoulder[0]) / 2)
            shoulder_mid_y = int((right_shoulder[1] + left_shoulder[1]) / 2)

            if (gameState == 2):
                drawHandLine(img)

        key = cv2.pollKey()
        if (key == 27):
            break
        elif (key == 32):
            if gameState == 0:
                gameState = 1
                counter = 5
        screenY = int(cv2.getWindowImageRect('Frame')[2] / 2)
        screenX = int(cv2.getWindowImageRect('Frame')[3] / 2)
        deltaTime = time.time() - currentTime

        _, buffer = cv2.imencode('.jpg', img)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
