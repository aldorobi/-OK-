import cv2

img = cv2.imread('poster.jpg')

rocket = img[120:360,400:500]
img[0:240,500:600] = rocket

text = 'Hola,planeta.'

cv2.putText(img,
            text,
            (20,220),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 2,
            color = (0,255,0))

cv2.imshow('あ', img)

cv2.waitKey(0)