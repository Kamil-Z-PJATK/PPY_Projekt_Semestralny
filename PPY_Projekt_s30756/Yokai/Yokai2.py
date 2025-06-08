from Yokai.Yokai import Yokai


class Yokai2(Yokai):

    def __init__(self, hunger, fun, level ):
        imageList =[ "Images/Kitsune/Idle_2.png", "Images/Kitsune/Idle_3.png", "Images/Kitsune/Idle_4.png", "Images/Kitsune/Idle_5.png", "Images/Kitsune/Idle_6.png", "Images/Kitsune/Idle_7.png", "Images/Kitsune/Idle_8.png"]
        self.hunger = hunger*1
        self.fun = (float)(fun*1)
        self.hunger_per_tick = 1
        self.fun_per_tick = 1
        self.x = 350
        self.y = 200

        super().__init__("Yokai1", imageList,self.hunger,self.fun,self.hunger_per_tick,self.fun_per_tick,self.x,self.y, level)

