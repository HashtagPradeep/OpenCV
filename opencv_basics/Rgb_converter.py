import cv2

img = cv2.imread('D:\git_code\Joker\Joker.jpg',0)
# cv2.imshow("RGB Image",img)

imgrgb = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)

cv2.imshow("RGB Image",imgrgb)
cv2.waitKey(0)