import cv2 as cv #OpenCV 모듈 import
import sys #sys모듈 import

cap=cv.VideoCapture(0, cv.CAP_DSHOW) #카메라 연결, 비디오가 화면에 바로 나타나게 함

if not cap.isOpened :
    sys.exit('카메라 연결 실패') 

while True:
    ret,frame = cap.read() #비디오 구성하는 프레임 획득
    #ret: 카메라로부터 프레임 성공적으로 읽었는지 나타내는 변수

    if not ret:
        print('프레임 획득에 실패하여 루프 나감')
        break

    cv.imshow('Video display', frame)

    key = cv.waitKey(1) #1밀리초동안 키보드 입력 기다림
    if key == ord('q'): #'q'키가 들어오면 루프 빠져나감
        break

cap.release() #카메라 연결 해제
cv.destroyAllWindows()