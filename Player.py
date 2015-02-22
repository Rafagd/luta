# -*- coding: utf-8 -*-

class Player :
   
    def __init__(self, player_id, character):
        config          = Application.instance().config
        self.controller = KeyboardInput(config[player_id])
        self.character  = Character(character)

    def input(self, frame, event) :
        self.controller.check(frame, event)   
        
        last = self.controller.buffer[-1]

        if last[1] == 'left' and last[2] == -1 :
            self.character.walk_left()

        if last[1] == 'right' and last[2] == -1 :
            self.character.walk_right()
       
    def update(self, frame) :
        pass

    def draw(self, frame, window) :
        self.character.draw(frame, window)

from Application          import *
from inputs.KeyboardInput import *
from Character            import *
