import cv2

web_cam = cv2.VideoCapture(0)

while True:
    cap, frame = web_cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if cap == True:
        cv2.imshow('Hello', gray)

        if cv2.waitKey(48) & 0xFF == ord('q'):
            break
    else: 
        print('Hi!!')
        break