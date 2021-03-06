import cv2
import numpy as np
from kivymd.toast import toast


class erosion():
    def __init__(self):
        pass

    def process(self, file, extension):
        input_image = cv2.imread(file, cv2.IMREAD_COLOR)
        kernel = np.ones((5, 5), np.uint8)
        erosion_image = cv2.erode(input_image, kernel, iterations=1)

        cv2.imwrite('temp' + extension, erosion_image)
        toast("operation applied")

        print("opearation applied")
