import cv2
img=cv2.imread("sample2.jpg")
grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Orig",img)
cv2.imshow("Gray",grayImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
