#!/usr/bin/python
# -*- coding: utf-8 -*-

import sfml as sf
import aoko

input_free = True

class application :
    
    def __init__(self):
        self.window = sf.RenderWindow(sf.VideoMode(800, 600), "Game")

        self.image = sf.Image.from_file("aoko.png")
        self.image.create_mask_from_color(sf.Color(255, 255, 255))
        self.sprite = sf.Sprite(sf.Texture.from_image(self.image))
        self.sprite.ratio = sf.Vector2(2, 2)

        while self.window.is_open :
            self.read_input()
            self.update()
            self.draw()

            sf.sleep(sf.seconds(0.1))
        

    def read_input(self) :
        global input_free

        for event in self.window.events :
            if type(event) is sf.CloseEvent :
                self.window.close()

            if input_free == False and type(event) is sf.KeyEvent and not event.pressed :
                aoko.state = "idle"
                aoko.i = 0
                aoko.m = len(aoko.data[aoko.state]["frames"])
                input_free = True

            if input_free and type(event) is sf.KeyEvent and event.pressed and event.code is sf.Keyboard.SPACE :
                aoko.state = "walk"
                aoko.i = 0
                aoko.m = len(aoko.data[aoko.state]["frames"])
                input_free = False

    def update(self) :
        pass

    def draw(self) :
        self.window.clear()

        self.sprite.texture_rectangle = sf.Rectangle(
            sf.Vector2(aoko.data[aoko.state]["frames"][aoko.i]["x"], aoko.data[aoko.state]["frames"][aoko.i]["y"]),
            sf.Vector2(aoko.data[aoko.state]["frames"][aoko.i]["w"], aoko.data[aoko.state]["frames"][aoko.i]["h"])
        )

        self.window.draw(self.sprite)

        aoko.i = (aoko.i + 1) % aoko.m
        print self.sprite.texture_rectangle

        self.window.display()

application()
