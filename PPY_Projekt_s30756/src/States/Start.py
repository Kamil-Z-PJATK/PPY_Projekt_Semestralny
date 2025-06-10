import pygame

from src.Button import Button
from src.States.State import State


class Start(State):
    def __init__(self,display,gameStateManager, SCREEN_WIDTH,SCREEN_HEIGHT):
        """

        Inicjalizuje ekran startowy gry z tłem, tytułem i przyciskiem START GAME.

        Args:
            display: powierzchnia Pygame do rysowania.
            gameStateManager: obiekt zarządzający stanami gry.
            SCREEN_WIDTH: szerokość ekranu.
            SCREEN_HEIGHT: wysokość ekranu.

        """
        super().__init__(display,gameStateManager, SCREEN_WIDTH,SCREEN_HEIGHT )

        self.button=Button(self.SCREEN_WIDTH // 2 - 95, self.SCREEN_HEIGHT // 2 - 5, 200, 50,"START GAME")
        self.font = pygame.font.Font("Fonts/Midorima-PersonalUse-Regular.ttf", 100)

        self.mouse=pygame.mouse.get_pos()

        self.image = pygame.image.load("Images/Monastery_outside.png")

    def run(self):
        """

        Renderuje ekran startowy: tło, tytuł gry oraz przycisk START GAME.
        Obsługuje również aktualizację pozycji myszy i przycisku.
        """

        self.mouse = pygame.mouse.get_pos()
        self.display.blit(self.image, (0,0))
        #text_font = pygame.font.SysFont("\Fonts\Midorima-PersonalUse-Regular.ttf", 40)
        lines=["YOKAI", "MONASTERY"]

        text_centre=(self.SCREEN_WIDTH // 2+5, self.SCREEN_HEIGHT // 3 - 150)
        text1 = self.font.render(lines[0], True, "black")
        text1_rect = text1.get_rect(center=text_centre)
        self.display.blit(text1, text1_rect)

        text_centre=(self.SCREEN_WIDTH // 2+5 , self.SCREEN_HEIGHT // 3 -70)
        text2 = self.font.render(lines[1], True, "black")
        text2_rect = text2.get_rect(center=text_centre)
        self.display.blit(text2, text2_rect)

        text_centre=(self.SCREEN_WIDTH // 2 , self.SCREEN_HEIGHT // 3 -155)
        text3 = self.font.render(lines[0], True, "white")
        text3_rect = text3.get_rect(center=text_centre)
        self.display.blit(text3, text3_rect)

        text_centre=(self.SCREEN_WIDTH // 2 , self.SCREEN_HEIGHT // 3 -75)
        text4 = self.font.render(lines[1], True, "white")
        text4_rect = text4.get_rect(center=text_centre)
        self.display.blit(text4, text4_rect)

        self.button.draw(self.display)
        self.button.update()


    def handle_event(self, event):
        """
        Obsługuje zdarzenia wejściowe, np. kliknięcie przycisku START GAME.

        Args:
            event: (pygame.event.Event)obiekt zdarzenia Pygame.
        """

        res=self.button.event_handeler(event,self.mouse)
        if res:
            super().fade(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
            self.gameStateManager.set_state("menu")


