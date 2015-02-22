# -*- coding: utf-8 -*-

import json
import sfml as sf

class Application :
    _instance = None

    @classmethod
    def instance(klass) :
        if klass._instance == None :
            klass._instance = Application()
        return klass._instance

    def __init__(self):
        self.state  = None
        self.window = None

        f = open("config.json")
        self.config = json.load(f)
        f.close()

    def pre_load(self) :
        self.window = sf.RenderWindow(sf.VideoMode(800, 600), "Input Test")
        
        self.window.framerate_limit    = 60
        self.window.key_repeat_enabled = False

        self.window.clear(sf.Color(0, 0, 0))
        self.window.display()

    def input(self, frame) :
        for event in self.window.events :
            if type(event) == sf.CloseEvent :
                self.window.close()
                break

            elif type(event) == sf.KeyEvent :
                self.state.input(frame, event)

    def update(self, frame) :
        self.state.update(frame)

    def draw(self, frame) :
        self.window.clear(sf.Color(0, 0, 0))
        self.state.draw(frame, self.window)
        self.window.display()

    def run(self) :
        self.pre_load()

        self.state = FightState()

        clock  = sf.Clock();
        offset = clock.elapsed_time.seconds - int(clock.elapsed_time.seconds)

        last_frame = -1

        while self.window.is_open :
            frame = int((clock.elapsed_time.seconds - offset) / (1.0 / 60.0))

            self.input(frame)

            if frame != last_frame :
                self.update(frame)
                self.draw(frame)
           
            last_frame = frame
       
        f = open("log", "w+")
        json.dump(self.state.p1.controller.buffer, f, indent=True)
        f.close()

from FightState import *
