'''
$ python setup.py build
> https://cx-freeze.readthedocs.io/en/latest/distutils.html
'''

import os
import sys
from cx_Freeze import setup, Executable

includes = []
excludes = ['cx_Freeze','pydoc_data','setuptools','distutils','tkinter']
if sys.platform == "win32":
    packages = ['kivy','kivymd']
    excludes = ['cx_Freeze','pydoc_data','setuptools','distutils','tkinter','ffpyplayer']
    includefiles = ['comp/','data/','fonts/','main.kv']
    #add dlls
    for root, subdirectories, files in os.walk('dlls'):
        for file in files:
            includefiles.append(f'{root}/{file}')
else:
    packages = ['kivy','kivymd', 'ffpyplayer']
    includefiles = ['comp/','data/','fonts/','main.kv']
    excludes = ['cx_Freeze','pydoc_data','setuptools','distutils','tkinter']

base = None
shortcutName = None
shortcutDir = None
if sys.platform == "win32":
    base = "Win32GUI"
    shortcutName='Word Guide'
    shortcutDir="DesktopFolder"


setup(
    name = 'Word Guide',
    version = '0.1',
    description = 'Word Guide',
    author = 'ivansaul',
    author_email = '',
    options = {'build_exe': {
        'includes': includes,
        'excludes': excludes,
        'packages': packages,
        'include_files': includefiles}
        }, 
    executables = [Executable('main.py', 
    base = base, # "Console", base, # None
    icon='comp/icon-app.ico', 
    shortcutName = shortcutName, 
    shortcutDir = shortcutDir)]
)