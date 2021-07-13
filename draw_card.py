from PIL import Image
from image_utils import ImageText
from multiprocessing.dummy import Pool as ThreadPool

#draw_bg
def draw_bg(bg):
    #im = ImageText(Image.open(f"comp/{bg}.png").resize((511,638)))
    return ImageText(Image.open(f"comp/{bg}.png").resize((511,638)))

#word
def draw_word(im, text):   
    color = (75, 75, 75)
    font = 'fonts/ARIBLK.TTF'
    im.write_text((78,227-8), text.capitalize(), font_filename=font, font_size=33, color=color)

#pron
def draw_pron(im, text):
    text = f'[ {text[-1]} ]'
    color = (152, 136, 136)
    font = 'fonts/ARIAL.TTF'
    im.write_text((80,263), text, font_filename=font, font_size=12, color=color)

#sense
def draw_sense(im, text):
    text = ', '.join(text[:6])
    color = (152, 136, 136)
    font = 'fonts/Righteous-Regular.ttf'
    im.write_text_box((98,284-1), text, box_width=300, font_filename=font, font_size=11, color=color)

#eg_en
def draw_eg_en(im, text, xy, box_width):
    color = (75, 75, 75)
    font = 'fonts/Oduda-Bold.otf'
    im.write_text_box(xy, text.capitalize(), box_width=box_width, font_filename=font, font_size=20, color=color)

#eg_es
def draw_eg_es(im, text, xy, box_width):
    color = (152, 136, 136)
    font = 'fonts/FredokaOne-Regular.ttf'
    im.write_text_box(xy, text.capitalize(), box_width=box_width, font_filename=font, font_size=12, color=color)

#save
def draw_save(im, text):
    im.save(f'data/images/{text}.png')

#Worker 
def draw_card(example, index):
    if len(example[0])<=20:
        im = draw_bg(bg='bg1')
        draw_word(im=im, text=word)
        draw_pron(im=im, text=pron)
        draw_sense(im=im, text=sense)
        draw_eg_en(im=im, text=example[0], xy=(117,332-4), box_width=270)
        draw_eg_es(im=im, text=example[1], xy=(117,397-4), box_width=270)
        draw_save(im=im, text=f'wod_{index}')
    if 20<len(example[0])<=75:
        im = draw_bg(bg='bg2')
        draw_word(im=im, text=word)
        draw_pron(im=im, text=pron)
        draw_sense(im=im, text=sense)
        draw_eg_en(im=im, text=example[0], xy=(117,335-7), box_width=270)
        draw_eg_es(im=im, text=example[1], xy=(117,441-7), box_width=270)
        draw_save(im=im, text=f'wod_{index}')
    if len(example[0])>75:
        im = draw_bg(bg='bg3')
        draw_word(im=im, text=word)
        draw_pron(im=im, text=pron)
        draw_sense(im=im, text=sense)
        draw_eg_en(im=im, text=example[0], xy=(117,316-4), box_width=300)
        draw_eg_es(im=im, text=example[1], xy=(117,468-4), box_width=300)
        draw_save(im=im, text=f'wod_{index}')

#Read json data
import json
with open('data/words/wod.json', encoding='utf-8') as json_file:
    word_dic = json.load(json_file)

word = word_dic['word']
pron = word_dic['pron']
sense = word_dic['sense']

#Multiprocessing draw card
examples=word_dic['examples']
indices = [eg_idx for eg_idx in range(len(examples))]
pool = ThreadPool(10)
pool.starmap(draw_card, zip(examples, indices)) 
pool.close() 
pool.join()