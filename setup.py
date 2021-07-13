import sys
from cx_Freeze import setup, Executable


includefiles = ['comp/','data/','fonts/','draw_card.py','image_utils.py']
includes = []
excludes = ['cx_Freeze','pydoc_data','setuptools','distutils']
packages = []

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
    executables = [Executable('app.py', 
    base = base, 
    icon='comp/icon-app.ico', 
    shortcutName = shortcutName, 
    shortcutDir = shortcutDir)]
)