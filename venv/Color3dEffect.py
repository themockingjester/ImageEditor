from PIL import Image
from PIL import ImageFilter
from kivymd.toast import toast


class color3dEffect():
    def __init__(self):
        pass


    def process(self, file, extension):
        filename = file
        image = Image.open(filename)

        newimage = image.filter(ImageFilter.Color3DLUT)

        newimage.save('temp' + extension)
        toast("operation applied")
        print("operation applied")
