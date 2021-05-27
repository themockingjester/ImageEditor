import cv2
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.menu import MDDropdownMenu

from BlurEffect import blurEffect
from Color3dEffect import color3dEffect
from ContrastAdjustment import contrastAdjustment
from CountourEffect import countourEffect
from EdgeDetection import edgeDetection
from EdgeEnhance import edgeEnhance
from EdgeEnhanceMore import edgeEnhanceMore
from EmbossEffect import embossEffect
from Erosion import erosion
from FindEdges import findEdges
from FlipImage import flipImage
from GaussianBlur import gaussianBlurEffect
from GrayScale import grayScale
from ImgEnhanceColor import imgEnhanceColor
from InvertImage import invertImage
from MirrorImage import mirrorImage
from Sharpen import sharpenEffect
from Smooth import smoothEffect
from SmoothMore import smoothMoreEffect


class MainScreen(BoxLayout):
    filterapplyingbutton = ObjectProperty(None)
    mainimage = ObjectProperty(None)


class FileLoader(BoxLayout):
    filechooser = ObjectProperty(None)


class uiApp(MDApp):
    temporaryimage = "temp"
    temporaryimageextention = None
    realimage = None

    def filter_adder(self, instance):
        if uiApp.temporaryimageextention != None:

            for i in self.filters:
                if i.__name__ == instance.text:
                    print(i.__name__)
                    obj = i()
                    obj.process((uiApp.temporaryimage + uiApp.temporaryimageextention), uiApp.temporaryimageextention)
                    self.updateimage_at_canvas(uiApp.temporaryimage + uiApp.temporaryimageextention)
                    return 0
        else:
            toast("please select the image first")

    def updateimage_at_canvas(self, filename):
        self.mainscreen.mainimage.source = filename
        self.mainscreen.mainimage.reload()

    def reset_image(self):
        if uiApp.realimage != None:

            self.updateimage_at_canvas(uiApp.realimage)
            try:
                img = cv2.imread(uiApp.realimage)

                cv2.imwrite('temp' + uiApp.temporaryimageextention, img)

            except Exception as e:
                print(e)
        else:
            toast("you havn't selected any image")

    def load(self, path, filename):
        uiApp.temporaryimageextention = None
        if str(filename[0]).endswith('.png'):

            uiApp.temporaryimageextention = '.png'
        elif str(filename[0]).endswith('.jpg'):
            uiApp.temporaryimageextention = ".jpg"
        elif str(filename[0]).endswith('.jpeg'):
            uiApp.temporaryimageextention = ".jpeg"

        try:
            img = cv2.imread(filename[0])
            uiApp.realimage = filename[0]
            cv2.imwrite('temp' + uiApp.temporaryimageextention, img)
            self.updateimage_at_canvas(filename[0])
        except Exception as e:
            print(e)
            toast("something is wrong in this image")
        self.screen_manager.transition.direction = 'down'
        self.screen_manager.current = 'mainscreen'

    def build(self):

        self.screen_manager = ScreenManager()

        self.mainscreen = MainScreen()
        screen = Screen(name='mainscreen')
        screen.add_widget(self.mainscreen)
        self.screen_manager.add_widget(screen)

        self.fileloaderscreen = FileLoader()
        screen = Screen(name='fileloaderscreen')
        screen.add_widget(self.fileloaderscreen)
        self.screen_manager.add_widget(screen)

        self.filters = [contrastAdjustment, erosion, imgEnhanceColor, edgeDetection, grayScale, invertImage, flipImage,
                        mirrorImage,
                        countourEffect, blurEffect, embossEffect, color3dEffect, edgeEnhanceMore, edgeEnhance,
                        smoothMoreEffect, smoothEffect,
                        gaussianBlurEffect, sharpenEffect, findEdges]

        availablefilters = [{"text": i.__name__} for i in self.filters]

        self.filter_menu = MDDropdownMenu(
            callback=self.filter_adder, items=availablefilters, width_mult=5,
            caller=self.mainscreen.filterapplyingbutton
        )

        return self.screen_manager

    def mainscreen_to_fileloaderscreen(self):
        self.screen_manager.transition.direction = 'up'
        self.screen_manager.current = 'fileloaderscreen'

    def fileloaderscreen_to_mainscreen(self):
        self.screen_manager.transition.direction = 'down'
        self.screen_manager.current = 'mainscreen'


uiApp().run()
