from kivy.config import Config
from kivy.utils import platform

if platform in ['linux', 'win', 'macosx']:
    Config.set('graphics','resizable', False)

import os
import json
import random
import tarfile
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.core.audio import SoundLoader
from kivymd.toast import toast

if not os.path.isfile('data/words/favorites.json'):
    with open('data/words/favorites.json', 'w', encoding='utf-8') as f:
        json.dump({}, f, ensure_ascii=False, indent=4)

if not os.path.isdir('data/audio'):
    tar = tarfile.open('data/audio.tar.gz')
    tar.extractall(path='data/')
    tar.close()

if platform in ['linux', 'win', 'macosx']:
    #Window.size = (511,638)
    #Window.size= (226,420)
    Window.size= (240,420)

# Designate Our .kv design file 
#Builder.load_file('main.kv')

class MainScreen(MDFloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.trans_es = False
        self.n = 0
        self.wod = {}
        with open('data/words/words.json', encoding='utf-8') as json_file:
            d = json.load(json_file)
            d = random.sample(d, 1)[0]
        with open('data/words/wod.json', 'w', encoding='utf-8') as f:
            json.dump(d, f, ensure_ascii=False, indent=4)
            del(d)
        with open('data/words/wod.json', encoding='utf-8') as json_file:
            self.wod = json.load(json_file)
        
        self.favorites = {}
        with open('data/words/favorites.json', encoding='utf-8') as json_file:
            self.favorites = json.load(json_file)

        #init variables
        self.word = self.wod['word']
        self.pron = self.wod["pron"][-1]
        self.sense = ', '.join(self.wod['sense'][:6])
        self.examples = self.wod['examples']
        self.favorite_status = self.word in self.favorites
        
        
        self.ids.btn_heart.icon = 'heart'
        self.ids.lbl_word.text = self.word.capitalize()
        self.ids.lbl_pron.text = f'[ {self.pron} ]'
        self.ids.lbl_sense.text = self.sense
        self.ids.lbl_eg_en.text = self.examples[0][0].capitalize()
        

        ''' Formal all fields '''

        # favorite button status
        if self.favorite_status:
            self.ids.btn_heart.icon = 'heart'
        else:
            self.ids.btn_heart.icon ='heart-outline'
        
        # word label
        if len(self.ids.lbl_word.text) >= 11:
            self.ids.lbl_word.font_size = '29sp'
        
        # sense label
        if len(self.ids.lbl_sense.text) > 25:
            self.ids.lbl_sense.font_size = '11sp'
        
        # examples labels     
        if 20 < len(self.ids.lbl_eg_en.text) <= 75:
            self.ids.lbl_eg_en.font_size = '13.5sp'
        elif len(self.ids.lbl_eg_en.text) <= 20:
            self.ids.lbl_eg_en.font_size = '15sp'
        elif len(self.ids.lbl_eg_en.text) > 75:
            self.ids.lbl_eg_en.font_size = '10sp'
        

        #self.sound = SoundLoader.load('data/audio/about_us.ogg')
        #self.sound.play()

        print(self.wod['word'])

    def format_labels(self):
        # favorite button status
        if self.favorite_status:
            self.ids.btn_heart.icon = 'heart'
        else:
            self.ids.btn_heart.icon ='heart-outline'
        
        # word label
        if len(self.ids.lbl_word.text) >= 11:
            self.ids.lbl_word.font_size = '29sp'
        
        # sense label
        if len(self.ids.lbl_sense.text) > 25:
            self.ids.lbl_sense.font_size = '11sp'

    def format_examples(self):
        if 20 < len(self.ids.lbl_eg_en.text) <= 75:
            self.ids.lbl_eg_en.font_size = '13.5sp'
        elif len(self.ids.lbl_eg_en.text) <= 20:
            self.ids.lbl_eg_en.font_size = '15sp'
        elif len(self.ids.lbl_eg_en.text) > 75:
            self.ids.lbl_eg_en.font_size = '10sp'
    
    def next(self):
        self.trans_es = False
        self.n = (self.n + 1) % len(self.examples)
        print(self.n)
        print(self.examples[self.n])
        self.ids.lbl_eg_en.text = self.examples[self.n][0].capitalize()
        self.format_examples()
    
    
    def previous(self):
        self.trans_es = False
        self.n = (self.n - 1) % len(self.examples)
        print(self.n)
        print(self.examples[self.n])
        self.ids.lbl_eg_en.text = self.examples[self.n][0].capitalize()
        self.format_examples()
        
    
    def translate(self):
        self.trans_es = not self.trans_es
        if self.trans_es:
            self.ids.lbl_eg_en.text = self.examples[self.n][1].capitalize()
        else:
            self.ids.lbl_eg_en.text = self.examples[self.n][0].capitalize()

      
    def play_sound(self):
        #pip install ffpyplayer
        #link_us = self.word['us_ogg']
        link_us = f'data/audio/{self.word}_us.ogg'
        sound = SoundLoader.load(link_us)
        if sound:
            #sound.volume = 0.1
            sound.play()
    

    def add_favorites(self):  
        if self.word in self.favorites:
            print(f"Delete [ {self.word} ] from favorites")
            self.favorites.pop(self.word)
            self.ids.btn_heart.icon ='heart-outline'
        else:
            print(f"Add [ {self.word} ] to favorites")
            self.favorites[self.word] = self.wod
            self.ids.btn_heart.icon ='heart'

        with open('data/words/favorites.json', 'w', encoding='utf-8') as f:
            json.dump(self.favorites, f, ensure_ascii=False, indent=4)
                    

    def change(self):
        with open('data/words/words.json', encoding='utf-8') as json_file:
            d = json.load(json_file)
            d = random.sample(d, 1)[0]
        with open('data/words/wod.json', 'w', encoding='utf-8') as f:
            json.dump(d, f, ensure_ascii=False, indent=4)
            del(d)
        with open('data/words/wod.json', encoding='utf-8') as json_file:
            self.wod = json.load(json_file)
        
        self.word = self.wod['word']
        self.pron = self.wod["pron"][-1]
        self.sense = ', '.join(self.wod['sense'][:6])
        self.examples = self.wod['examples']
        self.favorite_status = self.word in self.favorites
        
        self.ids.btn_heart.icon = 'heart'
        self.ids.lbl_word.text = self.word.capitalize()
        self.ids.lbl_pron.text = f'[ {self.pron} ]'
        self.ids.lbl_sense.text = self.sense
        self.ids.lbl_eg_en.text = self.examples[0][0].capitalize()

        self.format_labels()
        self.format_examples()


    def change_favorite(self):
        try:
            with open('data/words/favorites.json', encoding='utf-8') as json_file:
                d = json.load(json_file)
                d = random.choice(list(d.values()))
            with open('data/words/wod.json', 'w', encoding='utf-8') as f:
                json.dump(d, f, ensure_ascii=False, indent=4)
                del(d)
            with open('data/words/wod.json', encoding='utf-8') as json_file:
                self.wod = json.load(json_file)
            
            self.word = self.wod['word']
            self.pron = self.wod["pron"][-1]
            self.sense = ', '.join(self.wod['sense'][:6])
            self.examples = self.wod['examples']
            self.favorite_status = self.word in self.favorites
            
            self.ids.btn_heart.icon = 'heart'
            self.ids.lbl_word.text = self.word.capitalize()
            self.ids.lbl_pron.text = f'[ {self.pron} ]'
            self.ids.lbl_sense.text = self.sense
            self.ids.lbl_eg_en.text = self.examples[0][0].capitalize()

            self.format_labels()
            self.format_examples()
        except:
            toast('First add words to your favorites')


class MainApp(MDApp):
    
    def build(self):
        self.title = 'WG'
        self.icon = 'comp/icon-app.ico'
        return MainScreen()

if __name__ == '__main__':
    MainApp().run()