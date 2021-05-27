from PIL import Image, ImageOps
from PIL import ImageFilter
from kivymd.toast import toast


class embossEffect():
    def __init__(self):
        pass

    def process(self, file, extension):
        filename = file
        image = Image.open(filename)

        gray_image = ImageOps.grayscale(image)

        newimage = gray_image.filter(ImageFilter.EMBOSS)

        newimage.save('temp' + extension)
        toast("operation applied")
        print("operation applied")
