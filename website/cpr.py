from flask import Flask, render_template, Response
from flask_cors import CORS
import cv2
from cvzone.PoseModule import PoseDetector

app = Flask(__name__)
CORS(app)

detector = PoseDetector()

# Open the camera
capture = cv2.VideoCapture(0)

def generate_frames():
    while True:
        success, img = capture.read()
        if not success:
            continue

        img = detector.findPose(img)
        lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False)

        if lmList:
            # Example: Using right shoulder (landmark 12) and left shoulder (landmark 11)
            # You might need to adjust the landmark indices based on your pose model
            right_shoulder = lmList[12]
            left_shoulder = lmList[11]

            # Estimate heart position (approximate and will vary per individual)
            heart_x = int((right_shoulder[0] + left_shoulder[0]) / 2)
            heart_y = int((right_shoulder[1] + left_shoulder[1]) / 2) + 200  # Adjust 20 as needed

            # Draw a circle at the estimated heart position
            cv2.circle(img, (heart_x, heart_y), 50, (0, 0, 255), -1)

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