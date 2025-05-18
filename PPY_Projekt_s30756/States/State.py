import pygame
class State:
    def __init__(self,display, gameStateManager ,SCREEN_WIDTH,SCREEN_HEIGHT):
        self.display = display
        self.gameStateManager = gameStateManager
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT

    def run(self):
        pass
    def handleEvent(self,event):
        pass

    def fade(self,width, height):
        fade = pygame.Surface((width, height))
        fade.fill((0, 0, 0))
        for alpha in range(0, 150):
            fade.set_alpha(alpha)
            self.display.blit(fade, (0, 0))
            pygame.display.update()
            pygame.time.delay(5)