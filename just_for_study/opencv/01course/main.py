import cv2 as cv

cv.namedWindow('new', cv.WINDOW_NORMAL)
cv.resizeWindow('new', 800, 600)
cv.imshow('new', 0)
key = cv.waitKey()
if key == 'q':
    cv.destroyAllWindows()