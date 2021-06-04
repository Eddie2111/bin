import cv2

face_cascade = cv2.CascadeClassifier('i:/Nikolai/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)


while True:
    _, img = cap.read()
    gray,faces = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA), face_cascade.detectMultiScale(gray, 1.1, 5)
    
    #faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    
    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.imshow('img', img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            cv2.destroyAllWindows()
            exit()
            
cap.release()
cv2.destroyAllWindows()
