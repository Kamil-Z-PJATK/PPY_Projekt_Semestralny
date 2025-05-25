from States.State import State
import pygame

class Level(State):
    def __init__(self,display,gameStateManager,SCREEN_WIDTH,SCREEN_HEIGHT):
        super().__init__(display,gameStateManager,SCREEN_WIDTH,SCREEN_HEIGHT)
        self.font = pygame.font.SysFont("comicsans", 30)
        self.button_rect = pygame.Rect(self.SCREEN_WIDTH // 2 - 100, self.SCREEN_HEIGHT // 2 + 175, 200, 50)




    def run(self):
        self.display.fill("blue")


    def handle_event(self, event):
        pass

