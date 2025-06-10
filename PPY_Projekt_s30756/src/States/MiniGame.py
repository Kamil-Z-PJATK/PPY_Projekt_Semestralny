import random

from src.States.State import State
import pygame

class MiniGame(State):
    def __init__(self,display,gameStateManager,SCREEN_WIDTH,SCREEN_HEIGHT):
        """

        Inicjalizuje mini-grę typu Snake.

        Args:
            display: (pygame.display)powierzchnia Pygame do rysowania.
            gameStateManager: obiekt zarządzający stanami gry.
            SCREEN_WIDTH: szerokość ekranu.
            SCREEN_HEIGHT: wysokość ekranu.

        """
        self.display = display
        self.gameStateManager = gameStateManager
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.clock = pygame.time.Clock()
        self.cell_size = 20
        self.running = True
        self.direction = pygame.K_RIGHT
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.food = self.place_food()
        self.score = 0
        self.font = pygame.font.SysFont(None, 36)
        self.image = pygame.image.load("Images/Courtyard.png")

    def reset_game(self):
        """
        Resetuje stan gry do wartości początkowych.
        """
        self.running = True
        self.direction = pygame.K_RIGHT
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.food = self.place_food()
        self.score = 0

    def place_food(self):
        """

        Losuje nowe położenie jedzenia, upewniając się, że nie koliduje z ciałem węża.

        Returns:
            Tuple (x, y) z pozycją jedzenia.

        """
        while True:
            x = random.randint(0, (self.SCREEN_WIDTH - self.cell_size) // self.cell_size) * self.cell_size
            y = random.randint(0, (self.SCREEN_HEIGHT - self.cell_size) // self.cell_size) * self.cell_size
            if (x, y) not in self.snake:
                return (x, y)

    def run(self):
        """
        Główna pętla gry. Aktualizuje stan gry, rysuje elementy i kontroluje tempo.

        Returns:
            False, jeśli gra się zakończyła.
            Wynik (score), jeśli gra trwa.
        """

        if(self.running == False):
            return False
        self.update()
        self.draw()
        self.clock.tick(10)
        self.get_running()
        return self.score


    def handle_event(self, event):
        """

        Obsługuje zdarzenia klawiatury do zmiany kierunku ruchu węża.

        Args:
            event: (pygame.event.Event)obiekt zdarzenia Pygame.

        """

        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                if ((event.key == pygame.K_UP and self.direction != pygame.K_DOWN) or
                    (event.key == pygame.K_DOWN and self.direction != pygame.K_UP) or
                    (event.key == pygame.K_LEFT and self.direction != pygame.K_RIGHT) or
                    (event.key == pygame.K_RIGHT and self.direction != pygame.K_LEFT)):
                    self.direction = event.key

    def get_running(self):
        """
        Zwraca informację, czy gra nadal trwa.
        """
        return self.running

    def update(self):
        """
        Aktualizuje pozycję węża, sprawdza kolizje, zjada jedzenie i aktualizuje wynik.
        """
        head_x, head_y = self.snake[0]
        if self.direction == pygame.K_UP:
            head_y -= self.cell_size
        elif self.direction == pygame.K_DOWN:
            head_y += self.cell_size
        elif self.direction == pygame.K_LEFT:
            head_x -= self.cell_size
        elif self.direction == pygame.K_RIGHT:
            head_x += self.cell_size

        new_head = (head_x, head_y)

        if head_x < 0 or head_x >= self.SCREEN_WIDTH or head_y < 0 or head_y >= self.SCREEN_HEIGHT:
            self.running = False
            self.gameStateManager.set_state("level")
            self.reset_game()
            return

        if(self.score ==10):
            self.running = False
            self.gameStateManager.set_state("level")
            self.reset_game()
            return
        if new_head in self.snake:
            self.running = False
            return


        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.food = self.place_food()
            self.score += 1
        else:
            self.snake.pop()

    def draw(self):
        """
        Rysuje tło, węża, jedzenie i wynik na ekranie.
        """
        self.display.blit(self.image, (0,0))
        for segment in self.snake:
            pygame.draw.rect(self.display, "black",
                             pygame.Rect(segment[0], segment[1], self.cell_size, self.cell_size))
            pygame.draw.rect(self.display, "pink",
                             pygame.Rect(segment[0], segment[1], self.cell_size-3, self.cell_size-3))
        pygame.draw.rect(self.display, "white",
                         pygame.Rect(self.food[0], self.food[1], self.cell_size, self.cell_size))
        pygame.draw.rect(self.display, "red",
                         pygame.Rect(self.food[0]+3, self.food[1]+3, self.cell_size-6, self.cell_size-6))

        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.display.blit(score_text, (10, 10))

        pygame.display.update()

    def get_score(self):
        """
        Zwraca aktualny wynik gracza.
        """
        return self.score