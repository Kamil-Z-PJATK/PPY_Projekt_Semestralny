import pygame

from Yokai.Yokai import Yokai


class Yokai1(Yokai):

    def __init__(self):
        imageList =["Images/ball.jpg"]
        super().__init__("Yokai1", imageList)