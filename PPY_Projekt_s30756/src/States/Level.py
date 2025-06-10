from src.States.State import State
import pygame

class Level(State):
    def __init__(self,display,gameStateManager,SCREEN_WIDTH,SCREEN_HEIGHT):
        """
        Inicjalizuje główny level gry.

        Args:
            display: (pygame.display)powierzchnia Pygame do rysowania.
            gameStateManager: obiekt zarządzający stanami gry.
            SCREEN_WIDTH: szerokość ekranu.
            SCREEN_HEIGHT: wysokość ekranu.
        """
        super().__init__(display,gameStateManager,SCREEN_WIDTH,SCREEN_HEIGHT)
        self.font = pygame.font.SysFont("comicsans", 30)
        self.button_rect = pygame.Rect(self.SCREEN_WIDTH // 2 - 100, self.SCREEN_HEIGHT // 2 + 175, 200, 50)

        self.image = pygame.image.load("Images/Monastery_stage.jpg")



    def run(self):
        """
        Renderuje tło poziomu gry.
        """
        self.display.blit(self.image, (0,0))


    def handle_event(self, event):
        """
        Obsługuje zdarzenia

        Args:
            event: (pygame.event.Event)obiekt zdarzenia Pygame.
        """
        pass

