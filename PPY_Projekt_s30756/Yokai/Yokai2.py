from Yokai.Yokai import Yokai


class Yokai2(Yokai):

    def __init__(self, hunger, fun, level ):
        imageList =["Images/ball.jpg"]
        self.hunger = hunger*0.5
        self.fun = (float)(fun*1)
        self.hunger_per_tick = 1
        self.fun_per_tick = 1
        self.x = 500
        self.y = 100

        super().__init__("Yokai1", imageList,self.hunger,self.fun,self.hunger_per_tick,self.fun_per_tick,self.x,self.y, level)

