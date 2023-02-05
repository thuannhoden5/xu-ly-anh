# import the
import cv2
import numpy as np





# Erosion
def erosion(pathname):
    kernel = np.ones((3, 3), np.uint8)
    img = cv2.imread(pathname, cv2.IMREAD_UNCHANGED)
    cv2.imshow("Binary Image", img)
    erosion = cv2.erode(img, kernel, iterations=1)
    cv2.imshow('Erosion Image', erosion)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Dilation
def dilation(pathname):
    kernel = np.ones((3, 3), np.uint8)
    img = cv2.imread(pathname, cv2.IMREAD_UNCHANGED)
    cv2.imshow("Binary Image", img)
    dilation = cv2.dilate(img, kernel, iterations=1)
    cv2.imshow('Dilation Image', dilation)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Opening
def opening(pathname):
    kernel = np.ones((3, 3), np.uint8)
    img = cv2.imread(pathname, cv2.IMREAD_UNCHANGED)
    cv2.imshow("Binary Image", img)
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    cv2.imshow("Opening Image", opening)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Closing
def closing(pathname):
    kernel = np.ones((3, 3), np.uint8)
    img = cv2.imread(pathname, cv2.IMREAD_UNCHANGED)
    cv2.imshow("Binary Image", img)
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("Closing Image", closing)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Hit-Miss
def hitmiss(pathname):
    kernel = np.ones((3, 3), np.uint8)
    img = cv2.imread(pathname, cv2.IMREAD_UNCHANGED)
    cv2.imshow("Binary Image", img)
    hitmiss = cv2.morphologyEx(img, cv2.MORPH_HITMISS, kernel)
    cv2.imshow("Hit-miss Image", hitmiss)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


