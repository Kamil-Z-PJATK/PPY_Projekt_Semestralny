
import pygame

from Player import Player

from Yokai.Yokai import Yokai
from Yokai.Yokai1 import Yokai1

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
background = pygame.image.load("Images/Monastery_inside.xcf")
all_sprites = pygame.sprite.Group()


running = True



# player=Player(100,100)
# all_sprites.add(player)
yokai = Yokai1()
all_sprites.add(yokai)
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if yokai.rect.collidepoint(event.pos):
                yokai.clicked()


    screen.blit(background, (0, 0))
    all_sprites.draw(screen)
    # RENDER YOUR GAME HERE



    pygame.display.flip()

    clock.tick(60)

pygame.quit()