import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()  # Initialize the Sprite superclass

        # Load an image for the sprite
        self.image = pygame.image.load("Images/ball.jpg")

        # Get the rect (for positioning and collision)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        # Example movement: Move right every frame
        self.rect.x += 1