import pygame
class State:
    def __init__(self,display, gameStateManager ,SCREEN_WIDTH,SCREEN_HEIGHT):
        """

        Inicjalizuje nowy stan gry.

        Args:
            display: (pygame.display)powierzchnia Pygame, na której rysowane są elementy gry.
            gameStateManager: obiekt zarządzający aktualnym stanem gry.
            SCREEN_WIDTH: szerokość ekranu gry.
            SCREEN_HEIGHT: wysokość ekranu gry.

        """
        self.display = display
        self.gameStateManager = gameStateManager
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT

    def run(self):
        """
        Główna logika stanu gry. Powinna być nadpisana w klasach dziedziczących.
         """

        pass
    def handleEvent(self,event):
        """

        Obsługuje zdarzenia (np. naciśnięcia klawiszy, ruchy myszy).
        Powinna być nadpisana w klasach dziedziczących.

        Args:
            event: (pygame.event.Event)obiekt zdarzenia Pygame.
        """
        pass

    def fade(self,width, height):
        """

        Tworzy efekt zanikania (fade-out) poprzez nakładanie półprzezroczystej czarnej powierzchni.

        Args:
            width: szerokość powierzchni do zanikania.
            height: wysokość powierzchni do zanikania.
        """
        fade = pygame.Surface((width, height))
        fade.fill((0, 0, 0))
        for alpha in range(0, 150):
            fade.set_alpha(alpha)
            self.display.blit(fade, (0, 0))
            pygame.display.update()
            pygame.time.delay(5)