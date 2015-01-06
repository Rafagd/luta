# -*- coding: utf-8 -*-

import json
import sfml as sf

class Application :
    _instance = None

    @classmethod
    def instance(klass) :
        print klass._instance
        if klass._instance == None :
            klass._instance = Application()
        return klass._instance

    def __init__(self):
        self.state  = None
        self.window = None

        f = open("config.json")
        self.config = json.load(f)
        f.close()

    def run(self) :
        self.window = sf.RenderWindow(sf.VideoMode(800, 600), "Input Test")
        self.state  = FightState()

        self.window.framerate_limit    = 60
        self.window.key_repeat_enabled = False

        clock  = sf.Clock();
        offset = clock.elapsed_time.seconds - int(clock.elapsed_time.seconds)

        last_frame = -1

        while self.window.is_open :
            frame = int((clock.elapsed_time.seconds - offset) / (1.0 / 60.0))

            for event in self.window.events :
   
                if type(event) == sf.CloseEvent :
                    self.window.close()
                    break

                elif type(event) == sf.KeyEvent and event.pressed and event.code == sf.Keyboard.ESCAPE :
                    self.window.close()
                    break

                elif type(event) == sf.KeyEvent :
                    self.state.input(frame, event)

            if frame != last_frame :
                self.state.update(frame)
                self.state.draw(frame, self.window)
           
            last_frame = frame
       
        f = open("log", "w+")
        json.dump(self.state.p1.controller.buffer, f, indent=True)
        f.close()

from FightState import *
