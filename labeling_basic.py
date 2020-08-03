import cv2
import numpy as np

def labeling_basic():
    src = np.array([[0, 0, 1, 1, 0, 0, 0, 0],
                    [1, 1, 1, 1, 0, 0, 1, 0],
                    [1, 1, 1, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 0, 1, 0],
                    [0, 0, 1, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0]]).astype(np.uint8)
    
    src = src * 255
    cnt, labels = cv2.connectedComponents(src)

    print('src: ')
    print(src)
    print('labels: ')
    print(labels)
    print('number of labels: ', cnt)

if __name__ == '__main__':
    labeling_basic()