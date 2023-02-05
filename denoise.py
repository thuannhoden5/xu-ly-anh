import cv2


def denoise(pathname):
    img = cv2.imread(pathname, 1)
    med = cv2.medianBlur(img, 3)
    cv2.imshow('Median', med)
    cv2.imshow("Normal", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
