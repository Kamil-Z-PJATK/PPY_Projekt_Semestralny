import pygame
from pygame import surface

from Button import Button
from States.MiniGame import MiniGame


class Yokai(pygame.sprite.Sprite):

    hunger =100
    fun=100
    def __init__(self, name, imageList, hunger, fun, hunger_per_second,fun_per_second, x, y, level):
        super().__init__()
        self.name = name
        self.imageList = imageList
        self.image = pygame.image.load(self.imageList[0]).convert_alpha()
        self.init_hunger=hunger
        self.init_fun=fun
        self.hunger = hunger
        self.fun = fun
        self.hunger_per_second = hunger_per_second
        self.fun_per_tick = fun_per_second
        self.rect = self.image.get_rect()
        self.last_update = pygame.time.get_ticks()
        self.font = pygame.font.Font("Fonts\Midorima-PersonalUse-Regular.ttf", 30)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.show_stats=False;
        self.level = level
        self.text_pos = self.rect.midbottom
        self.button_pos=self.rect.midtop
        self.feed_button=Button(self.button_pos[0]-105,self.button_pos[1]-55,100,50,"FEED")
        self.play_button=Button(self.button_pos[0]+5,self.button_pos[1]-55,100,50,"PLAY")
        self.mouse=pygame.mouse.get_pos()
        self.alive= True




    def update(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.last_update >=1000:
            if self.alive:
                self.hunger -= self.hunger_per_second
                self.fun -= self.fun_per_tick
                self.last_update = current_time
            else:
                self.hunger=0
                self.fun=0
        if self.hunger <= 0 or self.fun <= 0:
            self.alive = False
        self.feed_button.update()
        self.play_button.update()



    def draw(self, screen):
        self.mouse = pygame.mouse.get_pos()
        if self.show_stats:
            hunger_text = self.font.render(f"Hunger: {self.hunger}", True, "black")
            fun_text = self.font.render(f"Fun: {self.fun}", True, "black")

            screen.blit(hunger_text, (self.text_pos[0] - hunger_text.get_width() // 2, self.text_pos[1] + 5))
            screen.blit(fun_text, (self.text_pos[0] - fun_text.get_width() // 2, self.text_pos[1] + 5 + hunger_text.get_height()))
            self.feed_button.draw(screen)
            self.play_button.draw(screen)

        if not self.alive:
            dead_text = self.font.render("DEAD", True, "red")
            screen.blit(dead_text,(self.rect.midtop[0] - dead_text.get_width() // 2, self.rect.midtop[1] + 5 ) )



    def clicked(self):
        self.show_stats=not self.show_stats




    def handle_event(self, event):
        if self.alive:
            do_feed=self.feed_button.event_handeler(event,self.mouse)
            if(do_feed):
                self.hunger +=10
            if(self.hunger >self.init_hunger):
                self.hunger = self.init_hunger
            do_play=self.play_button.event_handeler(event,self.mouse)
            if(do_play):
                return "minigame"
            if(self.fun >self.init_fun):
                self.fun = self.init_fun

    def set_fun(self, add):
        self.fun += add
        if (self.fun > self.init_fun):
            self.fun = self.init_fun

    def get_status(self):
        return self.alive

    def set_hunger(self, hunger):
        self.hunger = hunger