
import pygame

from Player import Player
from States.EndScrean import EndScrean
from States.Level import Level
from States.MiniGame import MiniGame
from States.TestState import SnakeGame

from Yokai.Yokai import Yokai
from Yokai.Yokai1 import Yokai1
from Yokai.Yokai2 import Yokai2
from main import GameStateManager

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
background = pygame.image.load("Images/Monastery_inside.xcf")
all_sprites = pygame.sprite.Group()


running = True




manager=GameStateManager("minigame")

level = Level(screen,manager,1280,720)
minigame=MiniGame(screen,manager,1280,720)
end=EndScrean(screen,manager,1280,720)
yokai = Yokai1(5,100, level)

#yokai2 = Yokai2(100,100, level)
all_sprites.add(yokai)
#all_sprites.add(yokai2)
test=SnakeGame(screen,minigame,1280,720)

while running:

    # level.run()
    # pom= minigame.run()
    # if(pom==False):
    #     running=False
   #  test.run()
   #  minigame.update()
    end.run()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        # minigame.handle_event(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            for yok in all_sprites:
                if yok.rect.collidepoint(event.pos):
                    yok.clicked()




        for sprite in all_sprites:
            sprite.handle_event(event)



    all_sprites.update()
    # screen.blit(background, (0, 0))
    all_sprites.draw(screen)
    for sprite in all_sprites:
        sprite.draw(screen)

    pygame.display.update()
    clock.tick(60)

class GameStateManager:
    def __init__(self, currentState):
        self.currentState = currentState

    def get_state(self):
        return self.currentState

    def set_state(self, state):
        self.currentState = state



    pygame.display.flip()

    clock.tick(60)

pygame.quit()