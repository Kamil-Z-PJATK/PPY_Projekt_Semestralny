import pygame

from States.State import State


class Start(State):
    def __init__(self,display,gameStateManager, SCREEN_WIDTH,SCREEN_HEIGHT):
        super().__init__(display,gameStateManager, SCREEN_WIDTH,SCREEN_HEIGHT )

        self.button_rect = pygame.Rect(self.SCREEN_WIDTH // 2 - 100, self.SCREEN_HEIGHT // 2 - 10, 200, 50)
        self.button_shadow_rect=pygame.Rect(self.SCREEN_WIDTH // 2 - 95, self.SCREEN_HEIGHT // 2 - 5, 200, 50)
        self.font = pygame.font.Font("Fonts\Midorima-PersonalUse-Regular.ttf", 100)
        self.button_color = pygame.Color("white")
        self.text_color = pygame.Color("black")
        self.shadow_color = pygame.Color("black")
        self.mouse=pygame.mouse.get_pos()


    def run(self):

        self.mouse = pygame.mouse.get_pos()
        self.display.fill("red")
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

        button_font=pygame.font.Font("Fonts\Midorima-PersonalUse-Regular.ttf", 30)

        pygame.draw.rect(self.display, self.shadow_color, self.button_shadow_rect)
        pygame.draw.rect(self.display, self.button_color, self.button_rect)
        text_surface = button_font.render("START GAME", True, self.text_color)
        text_rect = text_surface.get_rect(center=self.button_rect.center)
        self.display.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):

                super().fade(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
                self.gameStateManager.set_state("menu")
        if self.button_rect.collidepoint(self.mouse):
            self.button_color = pygame.Color("black")
            self.text_color = pygame.Color("white")
            self.shadow_color = pygame.Color("white")
        else:
            self.button_color = pygame.Color("white")
            self.text_color = pygame.Color("black")
            self.shadow_color = pygame.Color("black")


