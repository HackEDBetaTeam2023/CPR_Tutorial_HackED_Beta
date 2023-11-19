# Using Opencv to make a better understanding to citizens how to do a CPR in realtime.
import cv2
import cvzone.PoseModule

from cvzone.PoseModule import PoseDetector

import math
detector = PoseDetector()

# open camera
capture = cv2.VideoCapture(0)
targetLimbs = []

# LIMBS TO SHOW FOR DEMO: 25 26 23 24 13 14 11 12 0

def limb_load():
    file = open('limb_save.txt', 'r')
    lines = ""
    for line in file.readlines():
        positions = line.strip("[]\n").split(', ')
        for i in range(0,3):
            positions[i] = int(positions[i])
        targetLimbs.append(positions)
    print(targetLimbs)

limb_load()

def limb_save(lmList):
    file = open("limb_save.txt", "w")
    for limb in lmList:
        if limb != lmList[-1]:
            file.write(str(limb) + "\n")
        else:
            file.write(str(limb))
    file.close()

while True:
    success, img = capture.read()
    if not success:
        continue

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
        shoulder_distance = math.sqrt((right_shoulder[0] - left_shoulder[0]) ** 2 +
                                      (right_shoulder[1] - left_shoulder[1]) ** 2)

        hip_distance = math.sqrt((right_hip[0] - left_hip[0]) ** 2 +
                                (right_hip[1] - left_hip[1]) ** 2)

        circle_radius = int(shoulder_distance / 10)
        #print(len(lmList))
        # Estimate heart position (approximate and will vary per individual)

        shoulder_mid_x = int((right_shoulder[0] + left_shoulder[0]) / 2)
        shoulder_mid_y = int((right_shoulder[1] + left_shoulder[1]) / 2)

        hip_mid_x = int((right_hip[0] + left_hip[0]) / 2)
        hip_mid_y = int((right_hip[1] + left_hip[1]) / 2)

        heart_x = shoulder_mid_x + int(shoulder_distance * 0.0)
        heart_y = shoulder_mid_y + int(shoulder_distance * 0.0)

        heartDist = hip_distance/50
        new_heart_x = ((1-heartDist)*shoulder_mid_x) + (heartDist*hip_mid_x)
        new_heart_y = ((1-heartDist)*shoulder_mid_y) + (heartDist*hip_mid_y)
        key = cv2.pollKey()

        if (key == 115):
            print("Saving Data")
            limb_save(lmList)

        #print(heart_y)# Adjust 20 as needed
        line = cv2.line(img, (shoulder_mid_x, shoulder_mid_y), (hip_mid_x, hip_mid_y), (255, 200, 200), 5)
        # Draw a circle at the estimated heart position
        cv2.circle(img, (int(new_heart_x), int(new_heart_y)), circle_radius, (0, 0, 255), -1)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break


capture.release()
cv2.destroyAllWindows()