import cv2
import numpy as np
from kivymd.toast import toast


class contrastAdjustment():
    def __init__(self):
        pass

    def process(self, file, extension):
        img = cv2.imread(file)
        contrast_img = cv2.addWeighted(img, 2.5, np.zeros(img.shape, img.dtype), 0, 0)
        cv2.imwrite('temp' + extension, contrast_img)
        toast("operation applied")
        print("opearation applied")
