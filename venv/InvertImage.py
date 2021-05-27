from PIL import Image, ImageOps

from kivymd.toast import toast


class invertImage():
    def __init__(self):
        pass

    def process(self, file, extension):
        filename = file
        image = Image.open(filename)

        newimage = ImageOps.invert(image)

        newimage.save('temp' + extension)
        toast("operation applied")
        print("operation applied")
