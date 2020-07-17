import sys
import cv2

# cat.jpg 파일 불러와 img 변수에 저장
img = cv2.imread('cat.jpg', flags=cv2.IMREAD_GRAYSCALE)
cv2.imwrite('cat1.jpg', img, params = None)
# 영상 파일 불러오기가 실패하면 img가 None이고 이 경우 메세지 출력하고 종료
if img is None:
    print('Image load failed!')
    sys.exit()

# image라는 이름의 새 창을 만들고 이 창에 img 영상 출력, 그리고 키보드 입력이 있을 때 까지 대기
cv2.namedWindow('image')
cv2.imshow('image', img)
cv2.waitKey()

# 모든 창 닫기
cv2.destroyAllWindows()