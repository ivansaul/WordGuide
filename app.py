import os
import json
import runpy
import pyglet
import random
import tarfile
import platform
from tkinter import *
from PIL import Image, ImageTk

def new_word():
    with open('data/words/words.json', encoding='utf-8') as json_file:
        d = json.load(json_file)
        d = random.sample(d, 1)[0]
    with open('data/words/wod.json', 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=4)
        
def read_word():
    global word
    with open('data/words/wod.json', encoding='utf-8') as json_file:
        word = json.load(json_file)
    print(word['word'])


def resize_image(root, copy_of_image, Label1):
    load=copy_of_image.resize((511,638))
    render=ImageTk.PhotoImage(load)
    img.configure(image=render)
    img.image= render

def next():
    global n
    global items_list

    n = (n + 1) % len(items_list)
    url=items_list[n]
    print(n, url)

    load = Image.open(url)
    copy_of_image=load.copy()
    render = ImageTk.PhotoImage(load)

    img1 = Label(root, image=render)
    img1.bind('<configure>', resize_image(root, copy_of_image, img))
    img1.pack()

def previus():
    global n
    global items_list

    n = (n - 1) % len(items_list)
    url=items_list[n]
    print(n, url)

    load = Image.open(url)
    copy_of_image=load.copy()
    render = ImageTk.PhotoImage(load)

    img2 = Label(root, image=render)
    img2.bind('<configure>', resize_image(root, copy_of_image, img))
    img2.pack()

def remove_images(src='./data/images'):
    fls = os.listdir(src)
    for fl in fls:
        if fl.endswith('.png'):
            os.remove(f'{src}/{fl}')

def add_images_items_list(src='./data/images'):
    global items_list
    items_list=[]
    fls = os.listdir(src)
    for fl in fls:
        if fl.endswith('.png'):
            items_list.append(f'{src}/{fl}')

def change():
    new_word()
    read_word()
    remove_images()
    runpy.run_path(path_name='draw_card.py')
    add_images_items_list()
    next()

def play_sound():
    try:
        link_us = f"data/audio/{word['word']}_us.ogg"
        song = pyglet.media.load(filename=link_us, streaming=True)
        song.play()
    except:
        link_us = word['us_ogg']
        song = pyglet.media.load(link_us)
        song.play()

def untar_audio():
    if not os.path.isdir('data/audio'):
        tar = tarfile.open('data/audio.tar.gz')
        tar.extractall(path='data/')
        tar.close()

#remove images
remove_images()

#get word
word={}
new_word()
read_word()

#untar audio
untar_audio()

#draw images
runpy.run_path(path_name='draw_card.py')

#tkinter window
root = Tk()
root.title("Word of the day")
root.geometry("511x638")

if platform.system().lower().startswith('linux'):
    img_icon = ImageTk.PhotoImage(file='comp/icon-app.ico')
    root.tk.call('wm', 'iconphoto', root._w, img_icon)

if platform.system().lower().startswith('win'):
    root.iconbitmap(bitmap='comp/icon.ico')   

#initial label
n=0
items_list = []
add_images_items_list() #add items to items_list[]
url=items_list[n]

load = Image.open(url).resize((511,638))
copy_of_image=load.copy()
render = ImageTk.PhotoImage(load)

img = Label(root, image=render)
img.bind('<configure>', resize_image(root, copy_of_image, img))
img.pack()

#Buttons
btn_img_next=PhotoImage(file='comp/next.png')
btn_next=Button(root,image=btn_img_next,borderwidth=0,bg='#ECECF5',command=next)
btn_next.place(x=430,y=304.706)

btn_img_previus=PhotoImage(file='comp/previus.png')
btn_previus=Button(root,image=btn_img_previus,borderwidth=0,bg='#ECECF5',command=previus)
btn_previus.place(x=35,y=304.706)

btn_img_audio=PhotoImage(file='comp/sound.png')
btn_previus=Button(root,image=btn_img_audio,borderwidth=0,bg='#ECECF5',command=play_sound)
btn_previus.place(x=221.078,y=527)

btn_img_new=PhotoImage(file='comp/new.png')
btn_new=Button(root,image=btn_img_new,borderwidth=0,bg='#ECECF5',command=change)
btn_new.place(x=35.338,y=560.619)

root.resizable(False, False) 
root.mainloop()