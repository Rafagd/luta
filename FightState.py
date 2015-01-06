# -*- coding: utf-8 -*-

class FightState :

    def __init__(self) :
        self.p1 = Player("player1", "aoko")
        self.p2 = Player("player2", "aoko")
       
    def input(self, frame, event) :
        self.p1.input(frame, event)
        self.p2.input(frame, event)

    def update(self, frame) :
        self.p1.update(frame)
        self.p2.update(frame)
        pass

    def draw(self, frame, window) :
        self.p1.draw(frame, window)
        self.p2.draw(frame, window)

from Player import *
