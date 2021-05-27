from kivy.uix.image import Image
from PIL import Image, ImageEnhance
from kivy.uix.image import Image
from kivymd.toast import toast


class imgEnhanceColor():
    def __init__(self):
        pass

    def process(self, file, extension):
        print("opearation applied")
        filename = file
        image = Image.open(filename)
        # size = width, height = image.size

        enhancer = ImageEnhance.Color(image)
        # if we give 0.0 then it will inhance in white and black
        image = enhancer.enhance(0.5)
        toast("operation applied")

        image.save('temp' + extension)
        print("opearation applied")
