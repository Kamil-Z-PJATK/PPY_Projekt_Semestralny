from States.State import State
import pygame

class Level(State):
    def __init__(self,display,gameStateManager,SCREEN_WIDTH,SCREEN_HEIGHT):
        super().__init__(display,gameStateManager,SCREEN_WIDTH,SCREEN_HEIGHT)
    def run(self):
        self.display.fill("blue")

    def handle_event(self, event):
        pass