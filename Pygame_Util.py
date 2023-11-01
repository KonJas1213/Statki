import pygame
from pygame import mixer

pygame.mixer.init()
click_sound = pygame.mixer.Sound('checkbox.mp3')

class button():
    def __init__(self, color, x, y, width, height, text="", size=60, font=None, outline=0):
        self.color = color                              # kolor przycisku
        self.x = x                                      # x pos
        self.y = y                                      # y pos
        self.width = width                              # szerokość przycisku
        self.height = height                            # wysokość przycisku
        self.text = text                                # teskt na przycisku
        self.size = size                                # wielkość tekstu
        self.font = pygame.font.SysFont(font, size)     # rodzaj czcionki
        self.outline = outline                          # szerokość obramowania

        self.but_rect = pygame.Rect(self.x, self.y, self.width, self.height)

    #Draws the button, outline may be provided
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.but_rect, self.outline)

        if self.text != "":
            text = self.font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    #Returns true if the given pos (either tuple or list) is over the button
    def isOver(self, pos):
            return (pos[0] > self.x and pos[0] < self.x + self.width and pos[1] > self.y and pos[1] < self.y + self.height)


class checkbox():
    def __init__(self, color , x, y, width, height, backgroundcolor = (255,255,255), checkcolor = (255,0,0), outline=1, check=False, text="", size=60, font=None, textGap = 10):
        self.x = x                                       # x pos
        self.y = y                                       # y pos
        self.width = width                               # szerokość
        self.height = height                             # wysokość
        self.outline = outline                           # grubośc obramowania
        self.color = color                               # color obramowania
        self.check = check                               # zmienna "czy zaznaczone"
        self.backgroundcolor = backgroundcolor           # kolor tła niezaznaczone
        self.checkcolor = checkcolor                     # kolor tła zaznaczone
        self.text = text                                 # tekst
        self.font = pygame.font.SysFont(font, size)      # rodzaj czcionki
        self.size = size                                 # rozmair tekstu
        self.textGap = textGap                           # odległość tekstu od obramowania

        self.check_rect = pygame.Rect(self.x, self.y, self.width, self.height)
    #Draws the checkbox
    def draw(self, win):
        but = button(self.color, self.x, self.y, self.width, self.height, outline=self.outline)
        but.draw(win)

        if self.text != "":
            text = self.font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (self.x + self.width+self.textGap, self.y + (self.height/2 - text.get_height()/2)))

        if self.check:
            # pygame.draw.line(win, (0, 0, 0), (self.x, self.y), (self.x + self.width - self.outline, self.y + self.height - self.outline))
            # pygame.draw.line(win, (0, 0, 0), (self.x - self.outline + self.width, self.y), (self.x, self.y + self.height - self.outline))
            pygame.draw.rect(win, self.checkcolor, (self.x + self.outline, self.y + self.outline, self.width - self.outline*2, self.height - self.outline*2))
        else:
            pygame.draw.rect(win, self.backgroundcolor, (self.x + self.outline, self.y + self.outline, self.width - self.outline*2, self.height - self.outline*2))

    #Returns true if the given pos (either tuple or list) is over the box
    def isOver(self, pos):
        return (pos[0] > self.x and pos[0] < self.x + self.width and pos[1] > self.y and pos[1] < self.y + self.height)
        
    #Returns wether the box is checked or not
    def isChecked(self):
        return self.check

    #Checks or unchecks the box
    def convert(self, win):
        self.check = not self.check
        self.draw(win)

        if self.check:
            click_sound.play()

    click_sound = pygame.mixer.Sound('checkbox.mp3')

class slider():
    def __init__(self, color , x, y, width, height, value = 0,  backgroundcolor = (255,255,255), outline=0):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        self.backgroundcolor = backgroundcolor
        self.outline = outline

        self.value = value
        self.conteiner_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.button_rect = pygame.Rect(self.x , self.y, self.height, self.height)

    def move_slider(self, screen, mpos):
        self.button_rect.centerx = mpos[0]
        self.draw(screen)
        
    #draw a slider    
    def draw(self, win):
        pygame.draw.rect(win, self.backgroundcolor, self.conteiner_rect)
        pygame.draw.rect(win, self.color,  self.button_rect)
    #sprawdzanie kolizji
    def isOver(self, pos):
        return (pos[0] > self.x and pos[0] < self.x + self.width and pos[1] > self.y and pos[1] < self.y + self.height)