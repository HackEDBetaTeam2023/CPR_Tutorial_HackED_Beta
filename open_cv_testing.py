# Using Opencv to make a better understanding to citizens how to do a CPR in realtime.
import time

import cv2

from cvzone.PoseModule import PoseDetector

import math
detector = PoseDetector()

# open camera
capture = cv2.VideoCapture(0)
targetLimbs = []


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

nextHandVel = -1.0
handVelocity = 0.0

prevRightHandPos = [0,0]
prevLeftHandPos = [0,0]
def handsTogether() -> bool:
    dist = math.sqrt((rightHandPos[0] - leftHandPos[0])**2 + (rightHandPos[1] - leftHandPos[1])**2)
    return dist < minHandDistance

def calculateHandVelocity():
    global handVelocity
    global prevLeftHandPos
    global prevRightHandPos
    distance_x_r = abs(rightHandPos[0] - prevRightHandPos[0])
    distance_y_r = abs(rightHandPos[1] - prevRightHandPos[1])
    handVelocity = distance_y_r/1
    prevRightHandPos = rightHandPos
    prevLeftHandPos = leftHandPos

def limb_save(lmList):
    file = open("limb_save.txt", "w")
    for limb in lmList:
        if limb != lmList[-1]:
            file.write(str(limb) + "\n")
        else:
            file.write(str(limb))
    file.close()

def skeleton_user_in_line(limb:tuple[int,(int,int)]):

    error = False
    for item in limb:
        index =
        distance_x = abs(item[0] - lmList[?])
        distance_y = abs(item[1] - lmList[?])
        if distance_x > 30 or  distance_y > 30:
            error = True
    if error != 0:
        return False
    else: return True


while True:
    success, img = capture.read()
    if not success:
        continue

    skeleton()

    img = detector.findPose(img,True)
    lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False)

    if lmList:
        # Example: Using right shoulder (landmark 12) and left shoulder (landmark 11)
        # You might need to adjust the landmark indices based on your pose model
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
            calculateHandVelocity()

        cv2.circle(img, (int(leftHandPos[0]), int(leftHandPos[1])), 10, handsColor, -1)
        cv2.circle(img, (int(rightHandPos[0]), int(rightHandPos[1])), 10, handsColor, -1)

        shoulder_distance = math.sqrt((right_shoulder[0] - left_shoulder[0]) ** 2 +
                                      (right_shoulder[1] - left_shoulder[1]) ** 2)

        hip_distance = math.sqrt((right_hip[0] - left_hip[0]) ** 2 +
                                (right_hip[1] - left_hip[1]) ** 2)

        shoulder_mid_x = int((right_shoulder[0] + left_shoulder[0]) / 2)
        shoulder_mid_y = int((right_shoulder[1] + left_shoulder[1]) / 2)

        key = cv2.pollKey()

        if (key == 115):
            print("Saving Data")
            limb_save(lmList)
    cv2.putText(img,str(handVelocity), (10,25),cv2.FONT_HERSHEY_PLAIN,1.5,(0,255,200),2,cv2.LINE_AA)
    ##img = cv2.resize(img,(800,700))
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break


capture.release()
cv2.destroyAllWindows()