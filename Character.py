# -*- coding: utf-8 -*-

import json
import sfml as sf

class Character :

    def __init__(self, name) :
        self.data   = None
        self.path   = "chars/" + name + "/"
        self.image  = None
        self.sprite = None

        self.position   = sf.Vector2(0, 0)
        self.walk_speed = 1

        self.state         = ""
        self.current_frame = 0
        self.frame_count   = 0

        f = open(self.path + "data.json")
        self.data = json.load(f)
        f.close()

        self.load_image()
        self.load_sprite()

        self.change_state("idle")

    def load_image(self) :
        self.image = sf.Image.from_file(self.path + self.data["image"])
        self.image.create_mask_from_color(sf.Color(0x00, 0xFF, 0x00))

    def load_sprite(self) :
        self.sprite       = sf.Sprite(sf.Texture.from_image(self.image))
        self.sprite.ratio = sf.Vector2(2, 2)

    def change_state(self, state) :
        self.state         = state
        self.current_frame = 0
        self.frame_count   = len(self.data[self.state]["frames"])

    def walk_left(self) :
        self.position.x -= self.walk_speed

    def walk_right(self) :
        self.position.x += self.walk_speed

    def draw(self, frame, window) :
        current_frame = self.data[self.state]["frames"][self.current_frame]

        self.sprite.texture_rectangle = sf.Rectangle(
            sf.Vector2(current_frame["x"], current_frame["y"]),
            sf.Vector2(current_frame["w"], current_frame["h"])
        )

        self.sprite.texture_rectangle.position += self.position

        window.draw(self.sprite)

        self.current_frame = (self.current_frame + 1) % self.frame_count
