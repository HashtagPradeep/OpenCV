import cv2

my_charminar = cv2.imread('charminar.jpg')
print(my_charminar.shape)
cv2.imshow('my pic', my_charminar)
cv2.waitKey(10000)

