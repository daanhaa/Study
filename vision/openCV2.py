import cv2 as cv #OpenCV 모듈 import
import sys #sys모듈 import

img = cv.imread('rose.png') #이미지 읽기

if img is None :
    sys.exit('이미지 존재 안함') #이미지 존재 안하면 sys 모듈 이용해서 프로그램 종료

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #BGR 이미지를 GRAY 이미지로
gray_small = cv.resize(gray, dsize=(0,0), fx=0.5, fy=0.5) # 이미지 사이즈 변경

cv.imwrite('rose_gray.jpg',gray)
cv.imwrite('rose_gray_small.jpg', gray_small)

cv.imshow('Color image', img)
cv.imshow('Gray image',gray)
cv.imshow('Gray image small', gray_small)

cv.waitKey()
cv.destroyAllWindows()