import sys
from cx_Freeze import setup, Executable


includefiles = ['comp/','data/','fonts/','main.kv']
includes = []
excludes = ['cx_Freeze','pydoc_data','setuptools','distutils']
packages = ['kivy','kivymd','ffpyplayer']

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
    base = base, 
    icon='comp/icon-app.ico', 
    shortcutName = shortcutName, 
    shortcutDir = shortcutDir)]
)