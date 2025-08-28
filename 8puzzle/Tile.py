import pygame

class Tile:
    def __init__(self, screen, color, x, y, size, num, text):
        self.screen = screen
        self.color = color
        self.size = size
        self.num = num
        self.x = x
        self.y = y
        self.text = text

    def Draw(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, self.size, self.size))
        
        if(self.num != 0):
            number = self.text.render(str(self.num), True, (0, 0, 0))
            self.screen.blit(number, (self.x + self.size / 2 - number.get_width() / 2, 
                                  self.y + self.size / 2 - number.get_height() / 2))