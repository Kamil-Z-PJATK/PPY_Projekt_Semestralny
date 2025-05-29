import pygame
import sys

from States.Level import Level
from States.MiniGame import MiniGame
from States.Start import Start
from States.UI import Menu
from Yokai.Yokai1 import Yokai1

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS=60



class Game:
    def __init__(self):
        pygame.init()
        self.all_sprites = pygame.sprite.Group()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("YOKAI MONASTERY")
        self.clock = pygame.time.Clock()
        self.gameStateManager= GameStateManager("start")
        self.start=Start(self.screen, self.gameStateManager,SCREEN_WIDTH, SCREEN_HEIGHT)
        self.level=Level(self.screen, self.gameStateManager,SCREEN_WIDTH,SCREEN_HEIGHT)
        self.menu=Menu(self.screen,self.gameStateManager,SCREEN_WIDTH,SCREEN_HEIGHT)
        self.minigame=MiniGame(self.screen,self.gameStateManager,SCREEN_WIDTH,SCREEN_HEIGHT)
        self.init_fun=100
        self.init_food = 100
        self.states = {"start":self.start,"level":self.level, "menu":self.menu, "minigame":self.minigame}
        self.yokai = Yokai1(100, 100, self.level)
        self.all_sprites.add(self.yokai)


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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.yokai.rect.collidepoint(event.pos):
                        self.yokai.clicked()
                for sprite in self.all_sprites:
                   game= sprite.handle_event(event)

                if (game=="minigame"):
                    self.gameStateManager.set_state("minigame")
            self.states[self.gameStateManager.get_state()].run()

            if(self.gameStateManager.get_state()=="level"):
                self.all_sprites.update()
                # screen.blit(background, (0, 0))
                self.all_sprites.draw(self.screen)
                for sprite in self.all_sprites:
                    sprite.draw(self.screen)

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