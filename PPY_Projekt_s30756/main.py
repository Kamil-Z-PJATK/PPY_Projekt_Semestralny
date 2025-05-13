import pygame
import sys

from States.Level import Level
from States.Start import Start

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS=60

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.gameStateManager= GameStateManager("start")
        self.start=Start(self.screen, self.gameStateManager,SCREEN_WIDTH, SCREEN_HEIGHT)
        self.level=Level(self.screen, self.gameStateManager,SCREEN_WIDTH,SCREEN_HEIGHT)

        self.states={"start":self.start,"level":self.level}

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.states[self.gameStateManager.get_state()].handle_event(event)

            self.states[self.gameStateManager.get_state()].run()

            pygame.display.update()
            self.clock.tick(FPS)



# class Level:
#     def __init__(self,display,gameStateManager):
#         self.display = display
#         gameStateManager = gameStateManager
#     def run(self):
#         self.display.fill("blue")
#
#     def handle_event(self, event):
#         pass

# class Start:
#     def __init__(self,display,gameStateManager):
#         self.display = display
#         gameStateManager = gameStateManager
#         self.gameStateManager = gameStateManager
#         self.button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 25, 200, 50)
#         self.font = pygame.font.SysFont(None, 40)
#     def run(self):
#         self.display.fill("red")
#         pygame.draw.rect(self.display, "white", self.button_rect)
#         text_surface = self.font.render("Start Game", True, "black")
#         text_rect = text_surface.get_rect(center=self.button_rect.center)
#         self.display.blit(text_surface, text_rect)
#
#     def handle_event(self, event):
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if self.button_rect.collidepoint(event.pos):
#                 self.gameStateManager.set_state("level")
#
#
#


class GameStateManager:
    def __init__(self, currentState):
        self.currentState = currentState

    def get_state(self):
        return self.currentState
    def set_state(self,state):
        self.currentState = state


if __name__ == '__main__':
    game = Game()
    game.run()