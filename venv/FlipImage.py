from PIL import Image, ImageOps

from kivymd.toast import toast


class flipImage():
    def __init__(self):
        pass

    def process(self, file, extension):
        filename = file
        image = Image.open(filename)

        newimage = ImageOps.flip(image)

        newimage.save('temp' + extension)
        toast("operation applied")
        print("operation applied")
