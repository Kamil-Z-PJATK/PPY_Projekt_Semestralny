import pygame
import random

from States.State import State


class SnakeGame(State):
    def __init__(self, display, gameStateManager, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__(display, gameStateManager, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.clock = pygame.time.Clock()
        self.cell_size = 20
        self.running = True
        self.direction = pygame.K_RIGHT
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.food = self.place_food()

    def place_food(self):
        while True:
            x = random.randint(0, (self.SCREEN_WIDTH - self.cell_size) // self.cell_size) * self.cell_size
            y = random.randint(0, (self.SCREEN_HEIGHT - self.cell_size) // self.cell_size) * self.cell_size
            if (x, y) not in self.snake:
                return (x, y)

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(10)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.handleEvent(event)

    def handleEvent(self, event):
        if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
            if (event.key == pygame.K_UP and self.direction != pygame.K_DOWN) or \
               (event.key == pygame.K_DOWN and self.direction != pygame.K_UP) or \
               (event.key == pygame.K_LEFT and self.direction != pygame.K_RIGHT) or \
               (event.key == pygame.K_RIGHT and self.direction != pygame.K_LEFT):
                self.direction = event.key

    def update(self):
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

        # Check collision with walls
        if head_x < 0 or head_x >= self.SCREEN_WIDTH or head_y < 0 or head_y >= self.SCREEN_HEIGHT:
            self.running = False
            return

        # Check collision with self
        if new_head in self.snake:
            self.running = False
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.food = self.place_food()
        else:
            self.snake.pop()

    def draw(self):
        self.display.fill((0, 0, 0))
        for segment in self.snake:
            pygame.draw.rect(self.display, (0, 255, 0), pygame.Rect(segment[0], segment[1], self.cell_size, self.cell_size))
        pygame.draw.rect(self.display, (255, 0, 0), pygame.Rect(self.food[0], self.food[1], self.cell_size, self.cell_size))
        pygame.display.update()
