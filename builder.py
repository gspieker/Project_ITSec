#%pip install pyinstaller
#%pip install cx_Freeze
# issues with the building 



import cx_freeze

setup(
    name="kl",
    version="1.0",
    description="Simple Keylogger",
    executables=[Executable('keylogger_game.py')],

)

