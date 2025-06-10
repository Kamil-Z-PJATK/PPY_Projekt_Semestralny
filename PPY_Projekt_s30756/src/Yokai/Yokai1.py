from src.Yokai.Yokai import Yokai


class Yokai1(Yokai):

    def __init__(self, hunger, fun, level ):
        """
        Inicjalizuje obiekt Yokai1 z konkretnymi wartościami głodu, zabawy, pozycji i animacji.

        Args:
        hunger: Bazowy poziom głodu.
        fun: Bazowy poziom zabawy.
        level: Aktualny poziom gry.

        """
        imageList =["Images/Crow/Idle_1.png", "Images/Crow/Idle_3.png", "Images/Crow/Idle_4.png", "Images/Crow/Idle_5.png", "Images/Crow/Idle_6.png"]
        self.hunger = hunger*0.5
        self.fun = (float)(fun*1)
        self.hunger_per_tick = 1
        self.fun_per_tick = 1
        self.x =100
        self.y = 200

        super().__init__("Yokai1", imageList,self.hunger,self.fun,self.hunger_per_tick,self.fun_per_tick,self.x,self.y, level)

