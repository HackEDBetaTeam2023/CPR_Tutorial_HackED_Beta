# Using Opencv to make a better understanding to citizens how to do a CPR in realtime.
import time
import cv2
from cvzone.PoseModule import PoseDetector
import math
detector = PoseDetector()

capture = cv2.VideoCapture(0)
targetLimbs = []
deltaTime = 0.0
counter = 5.0
gameState = 0
didWin = "Congratulations"
accuracy = 0
# LIMBS TO SHOW FOR DEMO: 25 26 23 24 13 14 11 12 0

def limb_load():
    file = open('limb_save.txt', 'r')
    for line in file.readlines():
        positions = line.strip("[]\n").split(', ')
        for i in range(0,3):
            positions[i] = int(positions[i])
        targetLimbs.append(positions)
    print(targetLimbs)

limb_load()

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
def limb_save(lmList):
    file = open("limb_save.txt", "w")
    for limb in lmList:
        if limb != lmList[-1]:
            file.write(str(limb) + "\n")
        else:
            file.write(str(limb))
    file.close()
def drawHandLine(img):
    global handLineOffset
    handLineOffset += 23.0 * (deltaTime*25)
    if (handLineOffset > 360):
        handLineOffset = 0
    pos = int(math.cos(math.radians(handLineOffset)) * 15)
    rightBarPos[0] = 100
    rightBarPos[1] = 225 + pos
    leftBarPos[0] = 275
    leftBarPos[1] = 225 + pos
    barColor = (255,255,255)
    if True:
        barColor = (61,235,69)

    cv2.line(img, (100, 225 + (pos)), (275, 225 + (pos)), barColor, 2)
    cv2.circle(img, (int(leftBarPos[0]), int(leftBarPos[1])), 10, barColor, -1)
    cv2.circle(img, (int(rightBarPos[0]), int(rightBarPos[1])), 10, barColor, -1)

cv2.namedWindow('Frame', cv2.WINDOW_NORMAL)
while True:
    currentTime = time.time()
    success, img = capture.read()
    if not success:
        continue

    img = detector.findPose(img,True)
    lmList, bboxInfo = detector.findPosition(img, bboxWithHands = False)
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
            cv2.putText(img, 'GET INTO POSITION', (27, 30), cv2.FONT_HERSHEY_PLAIN, 2, (52, 192, 235), 2, cv2.LINE_AA)
            cv2.putText(img, str(int(counter)), (165, 70), cv2.FONT_HERSHEY_PLAIN, 3, (52, 192, 235), 2, cv2.LINE_AA)
        if gameState == 2:
            cv2.putText(img, 'START COMPRESSIONS', (27, 30), cv2.FONT_HERSHEY_PLAIN, 2, (52, 192, 235), 2, cv2.LINE_AA)
            cv2.putText(img, str(int(counter)), (165, 70), cv2.FONT_HERSHEY_PLAIN, 3, (52, 192, 235), 2, cv2.LINE_AA)
        if gameState == 3:
            cv2.putText(img, f"{didWin}", (27, 30), cv2.FONT_HERSHEY_PLAIN, 2, (52, 192, 235), 2, cv2.LINE_AA)
            cv2.putText(img, f"Your Accuracy Was: {int(accuracy)}%", (27, 30), cv2.FONT_HERSHEY_PLAIN, 2, (52, 192, 235), 2, cv2.LINE_AA)
    else:
        cv2.putText(img, f"Press 'SPACE' to Start", (27, 30), cv2.FONT_HERSHEY_PLAIN, 2, (52, 192, 235), 2, cv2.LINE_AA)
    if lmList:
        right_shoulder = lmList[12]
        left_shoulder = lmList[11]

        right_hip = lmList[24]
        left_hip = lmList[23]
        lmList[23] = [30,20,20]

        leftHandPos = [(lmList[16][0] + lmList[18][0] + lmList[20][0] + lmList[22][0])/4,
                       (lmList[16][1] + lmList[18][1] + lmList[20][1] + lmList[22][1])/4]
        rightHandPos = [(lmList[15][0] + lmList[17][0] + lmList[19][0] + lmList[21][0])/4,
                       (lmList[15][1] + lmList[17][1] + lmList[19][1] + lmList[21][1])/4]

        handsColor = (0,0,0)

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
    if (key == 115):
        print("Saving Data")
        limb_save(lmList)
    elif (key == 27):
        break
    elif (key == 32):
        if gameState == 0:
            gameState = 1
            counter = 5

    #img = cv2.resize(img,(800,700))
    cv2.imshow("Frame", img)
    deltaTime = time.time() - currentTime

capture.release()
cv2.destroyAllWindows()