from Yokai.Yokai import Yokai


class Yokai3(Yokai):

    def __init__(self, hunger, fun, level ):
        imageList =["Images/Yamabushi/Idle_1.png","Images/Yamabushi/Idle_3.png","Images/Yamabushi/Idle_4.png","Images/Yamabushi/Idle_5.png"]
        self.hunger = hunger*0.75
        self.fun = (float)(fun*0.75)
        self.hunger_per_tick = 1
        self.fun_per_tick = 1
        self.x = 600
        self.y = 200

        super().__init__("Yokai1", imageList,self.hunger,self.fun,self.hunger_per_tick,self.fun_per_tick,self.x,self.y, level)

