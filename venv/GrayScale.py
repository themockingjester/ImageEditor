from PIL import Image, ImageOps

from kivymd.toast import toast


class grayScale():
    def __init__(self):
        pass

    def process(self, file, extension):
        filename = file
        image = Image.open(filename)

        # applying grayscale method
        gray_image = ImageOps.grayscale(image)

        gray_image.save('temp' + extension)
        toast("operation applied")
        print("operation applied")
