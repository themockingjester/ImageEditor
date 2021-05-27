from PIL import Image
from PIL import ImageFilter
from kivymd.toast import toast


class countourEffect():
    def __init__(self):
        pass

    def process(self, file, extension):
        filename = file
        image = Image.open(filename)

        newimage = image.filter(ImageFilter.CONTOUR)

        newimage.save('temp' + extension)
        toast("operation applied")
        print("operation applied")
