import cv2

#cap = cv2.VideoCapture("Resources/test_video.mp4")
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

while True:
    ret,frame =  cap.read()  #"Frame" will get the next frame in the camera (via "cap"). "Ret" will obtain return value from getting the camera frame, either true of false
    cv2.imshow("Video",frame)
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()