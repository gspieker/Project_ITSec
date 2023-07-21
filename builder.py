#%pip install pyinstaller
#%pip install cx_Freeze
# issues with the building 

import PyInstaller.__main__ as pyi

pyi.run([
    'keylogger_Pynput.py',
    '--name=kl',
    '--onefile',
    '--console',
    '--version=1.0',
    '--description=IT Sec Key logger'
])
