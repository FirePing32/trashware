import cv2

cap = cv2.VideoCapture(0)

while(True):
    
    ret, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

    cv2.imshow('Trashware', rgb)

    out = cv2.imwrite('capture.jpg', frame)
    break

cap.release()
cv2.destroyAllWindows()