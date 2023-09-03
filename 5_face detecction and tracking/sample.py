import cv2
alg=".\haarcascadeface.xml"
haar_cascade = cv2.CascadeClassifier(alg)

cam = cv2.VideoCapture(2)

while True:
    _,img = cam.read()
    grayImg = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    face =haar_cascade.detectMultiScale(grayImg,1.3,4)
    for(x,y,w,h) in face :
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

        cv2.imshow("FaceDetection",img)
        key  =cv2.waitKey(10)
        if key == 27:
            break
        cam.release()
        cv2.destroyAllWindows()

