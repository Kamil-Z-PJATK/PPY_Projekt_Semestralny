import pygame
import sys

from src.States.EndScrean import EndScrean
from src.States.Level import Level
from src.States.MiniGame import MiniGame
from src.States.Start import Start
from src.States.UI import Menu
from src.Yokai.Yokai1 import Yokai1
from src.Yokai.Yokai2 import Yokai2
from src.Yokai.Yokai3 import Yokai3
from src.Yokai.Yokai4 import Yokai4

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS=60



class Game:
    def __init__(self):

        """
        Inicjalizuje główne komponenty gry YOKAI MONASTERY.

        Tworzy ekran gry, zegar, grupę sprite'ów, menedżer stanów gry oraz instancje różnych ekranów/stadiów gry:
        - ekran startowy
        - główny poziom gry
        - menu
        - minigra
        - ekran końcowy

        Dodatkowo ustawia podstawowe statystyki gracza i zmienne pomocnicze.
        """
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
        self.end=EndScrean(self.screen,self.gameStateManager,SCREEN_WIDTH,SCREEN_HEIGHT)
        self.init_fun=100
        self.init_food = 100
        self.states = {"start":self.start,"level":self.level, "menu":self.menu, "minigame":self.minigame, "end":self.end}

        self.added=0
        self.score=-1
        self.gamer=None
        self.ile=0
        

    def run(self):
        """

        Główna pętla gry. Obsługuje:
        - zdarzenia użytkownika (np.  zamknięcie okna),
        - logikę stanu gry i jego przełączanie,
        - interakcję sprite'ów z użytkownikiem,
        - aktualizację i rysowanie sprite'ów,
        - przejście do stanu końcowego gry, jeśli wszystkie postacie znikną.
        """
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.states[self.gameStateManager.get_state()].handle_event(event)
                if(self.gameStateManager.get_state()=="menu"):
                    self.init_food= self.states[self.gameStateManager.get_state()].return_value_food()
                    self.init_fun= self.states[self.gameStateManager.get_state()].return_value_fun()

                for sprite in self.all_sprites:
                    if event.type == pygame.MOUSEBUTTONDOWN:

                        if sprite.rect.collidepoint(event.pos):
                            sprite.clicked()
                for sprite in self.all_sprites:
                    game= sprite.handle_event(event)
                    if (game == "minigame"):
                        self.gameStateManager.set_state("minigame")
                        self.gamer=sprite

            if(self.gameStateManager.get_state()=="menu"):
                for sprite in self.all_sprites:
                    sprite.set_hunger(self.init_food)




            score=self.states[self.gameStateManager.get_state()].run()

            if(self.gameStateManager.get_state()=="minigame"):
                if(score!= None):
                    self.score=score

            if(self.gameStateManager.get_state()!="minigame" and self.score!=None and self.score!=-1):
                self.gamer.set_fun(10+self.score)
                self.score=-1


            if(self.gameStateManager.get_state()=="level"):
                self.all_sprites.update()

                self.all_sprites.draw(self.screen)

                if self.added==0:
                    yokai_1 = Yokai1(self.init_food, self.init_fun, self.level)
                    yokai_2 = Yokai2(self.init_food, self.init_fun, self.level)
                    yokai_3= Yokai3(self.init_food, self.init_fun, self.level)
                    yokai_4= Yokai4(self.init_food, self.init_fun, self.level)
                    self.all_sprites.add(yokai_1)
                    self.all_sprites.add(yokai_2)
                    self.all_sprites.add(yokai_3)
                    self.all_sprites.add(yokai_4)
                    self.added+=1

                for sprite in self.all_sprites:
                    sprite.draw(self.screen)


            pygame.display.update()

            if len(self.all_sprites)>0:
                for sprite in self.all_sprites:
                    #print(sprite.get_status())
                    if sprite.get_status()==False:
                        self.ile += 1


                if self.ile >= len(self.all_sprites):
                    self.gameStateManager.set_state("end")

            self.ile = 0

            self.clock.tick(FPS)




class GameStateManager:
    """
    Zarządza aktualnym stanem gry (np. start, menu, level, minigame, end screan).

    Umożliwia pobieranie i ustawianie aktywnego stanu.
    """
    def __init__(self, currentState):
        """

        Inicjalizuje menedżer stanu gry z podanym stanem początkowym.

        Args:
            currentState: (str) nazwa sceny do zapamiętania
        """
        self.currentState = currentState

    def get_state(self):
        """
        Zwraca aktualny stan gry.

        Returns:
            (str) Aktualny stan gry.

        """
        return self.currentState
    def set_state(self,state):
        """
        Ustawia nowy stan gry.

        Args:
         state: (str) Nowy stan gry do ustawienia.
        """
        self.currentState = state


if __name__ == '__main__':
    game = Game()
    game.run()