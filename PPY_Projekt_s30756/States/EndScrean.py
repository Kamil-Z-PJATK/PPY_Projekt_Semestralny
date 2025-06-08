import sys

import pygame

from Button import Button
from States.State import State


class EndScrean(State):
    def __init__(self,display,gameStateManager,SCREEN_WIDTH,SCREEN_HEIGHT):
        super().__init__(display,gameStateManager,SCREEN_WIDTH,SCREEN_HEIGHT)
        self.font = pygame.font.Font("Fonts\Midorima-PersonalUse-Regular.ttf", 60)

        self.button=Button(self.SCREEN_WIDTH // 2 - 100, self.SCREEN_HEIGHT // 2 + 175, 200, 50, "EXIT")
        self.mouse=pygame.mouse.get_pos()
        self.image = pygame.image.load("Images/Graveyard.jpg")


    def run(self):
        self.display.blit(self.image, (0,0))
        self.mouse=pygame.mouse.get_pos()
        text_surface = self.font.render("GAME OVER", True, "red")
        text_shadow = self.font.render("GAME OVER", True, "black")

        text_rect = text_surface.get_rect(center=(self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2 - 50))
        text_shadow_rect = text_shadow.get_rect(center=(self.SCREEN_WIDTH // 2+5, self.SCREEN_HEIGHT // 2 - 45))

        self.display.blit(text_shadow, text_shadow_rect)
        self.display.blit(text_surface, text_rect)


        self.button.draw(self.display)

    def handle_event(self, event):

        res=self.button.event_handeler(event,self.mouse)
        if res==True:
            pygame.quit()
