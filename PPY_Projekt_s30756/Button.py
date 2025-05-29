import time

import pygame


class Button:
    def __init__(self, x, y, width, height, text):

        self.button = pygame.Rect(x, y, width, height)
        self.shadow=pygame.Rect(x+5, y+5, width, height)
        self.font = pygame.font.Font("Fonts\Midorima-PersonalUse-Regular.ttf", 30)
        self.text=text
        self.colour = pygame.Color("white")
        self.shadow_color = pygame.Color("black")
        self. text_color=pygame.Color("black")
        self.last_pressed_time = 0
        self.active = True

    def draw(self,screen):
        pygame.draw.rect(screen, self.shadow_color, self.shadow)
        pygame.draw.rect(screen,self.colour,self.button)
        surface=self.font.render(self.text, False, self.text_color)
        text_rect = surface.get_rect(center=self.button.center)
        screen.blit(surface,text_rect )

    def event_handeler(self, event, mouse):
        if self.button.collidepoint(mouse) :
            self.colour=pygame.Color("black")
            self.shadow_color=pygame.Color("white")
            self.text_color=pygame.Color("white")
            # self.last_pressed_time=time.time()
            # self.active=False


        else:
            self.colour = pygame.Color("white")
            self.shadow_color=pygame.Color("black")
            self.text_color=pygame.Color("black")

        if event.type == pygame.MOUSEBUTTONDOWN and self.active:
            if self.button.collidepoint(event.pos):
                self.last_pressed_time=time.time()
                self.active=False
                return True

    def update(self):
        if not self.active and (time.time() - self.last_pressed_time) >= 4:
            self.active = True
