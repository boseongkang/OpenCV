import numpy as np
import cv2

def on_hue_changed(_=None):
    lower_hue = cv2.getTrackbarPos('Lower Hue','mask')
    upper_hue = cv2.getTrackbarPos('Upper Hue','mask')

    lowerb = (lower_hue, 100, 0)
    upperb = (upper_hue, 255, 255)
    mask = cv2.inRange(src_hsv, lowerb, upperb)

    cv2.imshow('mask', mask)

def main():

    global src_hsv

    src = cv2.imread('res/candies.png')

    if src is None:
        print('Image load failed')
        return

    src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

    cv2.imshow('src', src)

    cv2.namedWindow('mask')
    cv2.createTrackbar('Lower Hue', 'mask', 40, 179, on_hue_changed)    
    cv2.createTrackbar('Upper Hue', 'mask', 80, 179, on_hue_changed)
    on_hue_changed(0)

    cv2.waitKey()

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()



ref = cv2.imread('res/ref.png', cv2.IMREAD_COLOR)
mask = cv2.imread('res/mask.bmp', cv2.IMREAD_GRAYSCALE)
ref_ycrcb = cv2.cvtColor(ref, cv2.COLOR_BGR2YCrCb)

channels = [1, 2]
cr_bins = 128
cb_bins = 128
histSize = [cr_bins, cb_bins]

cr_range = [0, 256]
cb_range = [0, 256]
ranges = cr_range + cb_range

hist = cv2.calcHist([ref_ycrcb], channels, mask, histSize, ranges)

#Apply histogram backprojection to an input image

src = cv2.imread('res/kids.png', cv2.IMREAD_COLOR)
src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

# 색상 컬러에 기반한 얼굴검출 알고리즘
backproj = cv2.calcBackProject([src_ycrcb], channels, hist, ranges, 1)

cv2.imshow('src', src)
cv2.imshow('backproj', backproj)
cv2.waitKey()
cv2.destrotyAllWindows()
