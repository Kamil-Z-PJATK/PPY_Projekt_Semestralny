from Yokai.Yokai import Yokai


class Yokai4(Yokai):

    def __init__(self, hunger, fun, level ):
        imageList =["Images/Samurai/Idle_1.png","Images/Samurai/Idle_2.png", "Images/Samurai/Idle_3.png","Images/Samurai/Idle_5.png"]
        self.hunger = hunger*0.5
        self.fun = (float)(fun*0.5)
        self.hunger_per_tick = 1
        self.fun_per_tick = 1
        self.x = 850
        self.y = 200

        super().__init__("Yokai1", imageList,self.hunger,self.fun,self.hunger_per_tick,self.fun_per_tick,self.x,self.y, level)

