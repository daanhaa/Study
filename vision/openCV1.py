import cv2 as cv #OpenCV 모듈 import
import sys #sys모듈 import

img = cv.imread('rose.png') #이미지 읽기

if img is None :
    sys.exit('이미지 존재 안함') #이미지 존재 안하면 sys 모듈 이용해서 프로그램 종료

cv.imshow('Image display', img) #Image Display 

cv.waitKey() 
cv.destroyAllWindows() 

print(type(img)) 
print(img.shape) 