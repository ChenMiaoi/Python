import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

'''
cv.namedWindow('new', cv.WINDOW_NORMAL)
cv.resizeWindow('new', 800, 600)
cv.imshow('new', 0)
key = cv.waitKey()
if key == 'q':
    cv.destroyAllWindows()
'''
'''
img = cv.imread('/home/zack/图片/wallPaper/wallhaven-dgj3qj.jpg')
# plt.imshow(img)
cv.imshow('new', img)
key = cv.waitKey()
if key == 'q':
    cv.destroyAllWindows()
'''

cv.namedWindow('img', cv.WINDOW_NORMAL)
cv.resizeWindow('img', 320, 240)

img = cv.imread('/home/zack/图片/wallPaper/wallhaven-dgj3qj.jpg')

while True:
    cv.imshow('img', img)
    key = cv.waitKey(0)
    if key & 0xFF == ord('q'):
        break
    elif key & 0xFF == ord('s') :
        cv.imwrite('img01.png', img)
    else:
        print(key)
cv.destroyAllWindows()
