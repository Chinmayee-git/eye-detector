import cv2

data = cv2.CascadeClassifier('C:/chinmayee/python/eye_detector/eyes.xml')

image = cv2.imread('C:/chinmayee/python/eye_detector/face.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
eyes = data.detectMultiScale(gray_image)

for x in eyes:
    cv2.rectangle(image, (x[0], x[1]), (x[0]+x[2], x[1]+x[3]), (0, 255, 0), 2)

cv2.imshow('eyes', image)
cv2.waitKey()

print('code completed')