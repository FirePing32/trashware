import cv2

cap = cv2.VideoCapture(0) #var holding VideoCapture mode

while(True):
    
    ret, frame = cap.read() #reading graphical data
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA) #color of window frame

    cv2.imshow('Trashware', rgb) #title of window frame

    out = cv2.imwrite('capture.jpg', frame) #saving image
    break

#exiting
cap.release()
cv2.destroyAllWindows()