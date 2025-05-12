import pygame


class Yokai(pygame.sprite.Sprite):

    hunger =100
    fun=100
    def __init__(self, name, imageList ):
        super().__init__()
        self.name = name
        self.imageList = imageList
        self.image = pygame.image.load(self.imageList[0]).convert_alpha()
        self.rect = self.image.get_rect()


    def update(self):
        pass

    def clicked(self):
        print(f"""Yokai Clicked
Hunger: {self.hunger},
Fun: {self.fun}""")

