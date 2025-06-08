import pygame
from pygame import display

from Button import Button
from States.State import State


class Menu(State):
    def __init__(self,display,gameStateManager,SCREEN_WIDTH,SCREEN_HEIGHT, bg="gray"):
        super().__init__(display,gameStateManager,SCREEN_WIDTH,SCREEN_HEIGHT)
        self.font=pygame.font.Font("Fonts\Midorima-PersonalUse-Regular.ttf", 40)
        self.display = display
        self.bg = bg
        self.center1 = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2-50)
        self.center2 = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2+80)
        self.sliders = [
            Slider(self.center1, (200, 60), 0.5, 100, 200),
            Slider(self.center2, (200, 60), 0.5, 100, 200)
        ]

        self.text_centre=(self.sliders[0].slider_left-20, self.sliders[0].slider_top - 50)
        self.text_centre2=(self.sliders[1].slider_left+5, self.sliders[1].slider_top - 50)

        self.text_surface = self.font.render("INITIAL HUNGER", True, "white")
        self.text_shadow1=self.font.render("INITIAL HUNGER", True, "black")
        self.text_surface2= self.font.render("INITIAL FUN", True, "white")
        self.text_shadow2=self.font.render("INITIAL FUN", True, "black")

        self.options_font=pygame.font.Font("Fonts\Midorima-PersonalUse-Regular.ttf", 100)
        self.name_text = self.options_font.render("OPTIONS", True, "white")
        self.name_shadow = self.options_font.render("OPTIONS", True, "black")

        self.count_centre=(self.sliders[0].slider_right+10, self.sliders[0].slider_top+5)
        self.count_centre2=(self.sliders[1].slider_right+10, self.sliders[1].slider_top+5)


        self.button_shadow_rect=pygame.Rect(self.SCREEN_WIDTH // 2 - 95, self.SCREEN_HEIGHT // 2 +180, 200, 50)
        self.button=Button(self.SCREEN_WIDTH // 2 - 100, self.SCREEN_HEIGHT // 2 +175, 200, 50, "PLAY")
        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse = pygame.mouse.get_pressed()
        self.food=100
        self.fun=100
        self.image=pygame.image.load("Images/Monastery_inside.xcf")


    def run(self):
        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse=pygame.mouse.get_pressed()

        self.display.blit(self.image, (0,0))

        self.display.blit(self.name_shadow, (self.SCREEN_WIDTH //2 -165 , self.SCREEN_HEIGHT //3 -145))
        self.display.blit(self.name_text, (self.SCREEN_WIDTH //2 -170 , self.SCREEN_HEIGHT //3 -150))

        self.display.blit(self.text_shadow1, (self.text_centre[0]+5,self.text_centre[1]+5))
        self.display.blit(self.text_surface, self.text_centre)
        self.display.blit(self.text_shadow2,(self.text_centre2[0]+5,self.text_centre2[1]+5))
        self.display.blit(self.text_surface2, self.text_centre2)


        count_surface = self.font.render(f"{int(self.food.__round__(0))}", True, "white")
        count_shadow1 = self.font.render(f"{int(self.food.__round__(0))}", True, "black")
        count_surface2 = self.font.render(f"{int(self.fun.__round__(0))}", True, "white")
        count_shadow2 = self.font.render(f"{int(self.fun.__round__(0))}", True, "black")

        self.display.blit(count_shadow1, (self.count_centre[0] + 5, self.count_centre[1]+5))
        self.display.blit(count_surface, self.count_centre)
        self.display.blit(count_shadow2, (self.count_centre2[0] + 5, self.count_centre2[1]+5))
        self.display.blit(count_surface2, self.count_centre2)


        for slider in self.sliders:
            if slider.container.collidepoint(self.mouse_pos) and self.mouse[0]:
                slider.move_slider(self.mouse_pos)
            slider.render(self.display)
        self.food=self.sliders[0].get_value()
        self.fun=self.sliders[1].get_value()

        self.button.update()
        self.button.draw(self.display)
        pygame.display.flip()





    def handle_event(self, event):

        res=self.button.event_handeler(event,self.mouse_pos)

        if(res==True):
            super().fade(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
            self.gameStateManager.set_state("level")

    def return_value_food(self):
        return int(self.food.__round__(0))
    def return_value_fun(self):
        return int(self.fun.__round__(0))


class Slider:
    def __init__(self, pos:tuple, size:tuple, innit_value:float, min:int, max:int):
        self.pos = pos
        self.size = size

        self.min = min
        self.max = max

        self.slider_left=self.pos[0]-(self.size[0]//2)
        self.slider_right=self.pos[0]+(self.size[0]//2)
        self.slider_top=self.pos[1]-(self.size[1]//2)

        self.innit_value = (self.slider_right-self.slider_left)*innit_value

        self.container=pygame.Rect(self.slider_left, self.slider_top, self.size[0], self.size[1])
        self.shadow=pygame.Rect(self.slider_left+5, self.slider_top+5, self.size[0], self.size[1])
        self.button=pygame.Rect(self.slider_left+self.innit_value-5,self.slider_top,10,self.size[1])

    def move_slider(self, mouse_pos):
        self.button.centerx=mouse_pos[0]
    def render(self,display):
        pygame.draw.rect(display,"black",self.shadow)
        pygame.draw.rect(display, "lightgray",self.container)
        pygame.draw.rect(display, "red",self.button)
    def get_value(self):
        range=self.slider_right-self.slider_left -1
        button_value=self.button.centerx - self.slider_left
        return (button_value/range)*(self.max-self.min)+self.min

