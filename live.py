from kaki.app import App
from kivy.factory import Factory

from kivymd.app import MDApp
#For kivy use -> class MDLive(App)
#For kivymd use -> class MDLive(App, MDApp)
class MDLive(App, MDApp):
    KV_FILES = {
        'main.kv'
    }
    CLASSES = {
        'MainScreen': 'main'
    }
    AUTORELOADER_PATHS = [
        ('.',{'recursive':True})
    ]
    def build_app(self,*args):
        print('Hot Reload KivyMD App')
        return Factory.MainScreen()

MDLive().run()