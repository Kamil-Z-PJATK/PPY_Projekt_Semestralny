import pygame
import sys

from States.Level import Level
from States.Start import Start
from States.UI import Menu

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS=60



class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("YOKAI MONASTERY")
        self.clock = pygame.time.Clock()
        self.gameStateManager= GameStateManager("start")
        self.start=Start(self.screen, self.gameStateManager,SCREEN_WIDTH, SCREEN_HEIGHT)
        self.level=Level(self.screen, self.gameStateManager,SCREEN_WIDTH,SCREEN_HEIGHT)
        self.menu=Menu(self.screen,self.gameStateManager,SCREEN_WIDTH,SCREEN_HEIGHT)
        self.init_fun=100
        self.init_food = 100
        self.states = {"start":self.start,"level":self.level, "menu":self.menu}

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.states[self.gameStateManager.get_state()].handle_event(event)
                if(self.gameStateManager.get_state()=="menu"):
                    self.init_food= self.states[self.gameStateManager.get_state()].sliders[0].get_value()
                    self.init_fun= self.states[self.gameStateManager.get_state()].sliders[1].get_value()
                # print(self.init_food)
                # print(self.init_fun)
            self.states[self.gameStateManager.get_state()].run()

            pygame.display.update()
            self.clock.tick(FPS)




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