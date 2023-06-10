#%pip install pyinstaller
%pip install cx_Freeze


from cx_Freeze import setup, Executable

setup(
    name="kl",
    version="1.0",
    description="Simple Keylogger",
    executables=[Executable("/Users/georgespieker/Documents/GitHub/Project_One/keylogger_game.py.py")],
)

