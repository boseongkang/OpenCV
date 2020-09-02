import cv2
import numpy as np
import sys

def color_split():
    src = cv2.imread('res/candies.png', cv2.IMREAD_COLOR)

    if src is None:
        print('Image load failed!')
        return


    bgr_planes = cv2.split(src)    

    cv2.imshow('src', src)
    cv2.imshow('B_p', bgr_planes[0])
    cv2.imshow('G_p', bgr_planes[1])
    cv2.imshow('R_p', bgr_planes[2])

    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    color_split()