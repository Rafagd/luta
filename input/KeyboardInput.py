# -*- coding: utf-8 -*-

class KeyboardInput :

    def __init__(self, keys) :
        self.keys = keys
        self.repr = {}

        for k in keys :
            if (k != "confirm") and (k != "cancel") :
                self.repr[self.keys[k]] = k

        self.buffer        = [] # (frame, key, hold)
        self.buffer_offset = 0
        self.buffer_limit  = 30 # 500ms

    def check(self, frame, event) :
        try :
            key = self.repr[event.code]
        except :
            return

        try :
            last_frame = self.buffer[-1][0]
            last_key   = self.buffer[-1][1]
        except :
            last_frame = -1
            last_key   = -1

        valid_frame = frame - self.buffer_limit

        if event.pressed :
            if last_frame > valid_frame and key == last_key :
                return

            self.buffer.append((frame, key, -1))

        else :
            i = -1

            try :
                while i >= -len(self.buffer) :
                    current = self.buffer[i]

                    if current[1] == key :
                        self.buffer[i] = (
                            self.buffer[i][0],
                            self.buffer[i][1],
                            frame - self.buffer[i][0]
                        )
                        break
                    i -= 1
            except :
                pass

