import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eyes_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
cap=cv2.VideoCapture(0)
while True:
    _,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    faces = face_cascade.detectMultiScale(gray,1.1,4)
    eyes = eyes_cascade.detectMultiScale(gray,1.3,5)
    for x,y,w,h in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        # cv2.imshow('img',img)
        for ix,iy,iw,ih in eyes:
            cv2.rectangle(img,(ix,iy),(ix+iw,iy+ih),(255,0,0),2)
            cv2.imshow('img',img)
    if cv2.waitKey(2)==27:
        break
cap.release()
cv2.destroyAllWindows()