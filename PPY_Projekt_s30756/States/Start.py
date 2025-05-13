import pygame

from States.State import State


class Start(State):
    def __init__(self,display,gameStateManager, SCREEN_WIDTH,SCREEN_HEIGHT):
        super().__init__(display,gameStateManager, SCREEN_WIDTH,SCREEN_HEIGHT )

        self.button_rect = pygame.Rect(self.SCREEN_WIDTH // 2 - 100, self.SCREEN_HEIGHT // 2 - 25, 200, 50)
        self.font = pygame.font.SysFont(None, 40)
    def run(self):
        self.display.fill("red")
        pygame.draw.rect(self.display, "white", self.button_rect)
        text_surface = self.font.render("Start Game", True, "black")
        text_rect = text_surface.get_rect(center=self.button_rect.center)
        self.display.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                self.gameStateManager.set_state("level")

