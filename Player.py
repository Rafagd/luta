# -*- coding: utf-8 -*-

class Player :
   
    def __init__(self, player_id, character):
        config          = Application.instance().config
        self.controller = PlayerController(config[player_id])
        self.character  = Character(character)

    def input(self, frame, event) :
        self.controller.check(frame, event)   
       
    def update(self, frame) :
        pass

    def draw(self, frame, window) :
        self.character.draw(frame, window)

from Application      import *
from PlayerController import *
from Character        import *
