import sys

import pygame

from States.State import State


class EndScrean(State):
    def __init__(self,display,gameStateManager,SCREEN_WIDTH,SCREEN_HEIGHT):
        super().__init__(display,gameStateManager,SCREEN_WIDTH,SCREEN_HEIGHT)
        self.font = pygame.font.SysFont("comicsans", 60)
        self.button_rect = pygame.Rect(self.SCREEN_WIDTH // 2 - 100, self.SCREEN_HEIGHT // 2 + 175, 200, 50)





    def run(self):
        self.display.fill("BLACK")

        text_surface = self.font.render("GAME OVER", True, (255, 0, 0))
        text_rect = text_surface.get_rect(center=(self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2 - 50))
        self.display.blit(text_surface, text_rect)


        pygame.draw.rect(self.display, (255, 255, 255), self.button_rect)
        button_text = self.font.render("Exit", True, (0, 0, 0))
        button_text_rect = button_text.get_rect(center=self.button_rect.center)
        self.display.blit(button_text, button_text_rect)

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()
