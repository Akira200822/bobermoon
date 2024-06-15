import arcade

class Animation(arcade.Sprite):
    frame_index = 0
    time = 0

    def update_animation(self, delta_time):
        self.time += delta_time
        if self.time > 0.1:
            self.time = 0
            if self.frame_index == len(self.textures) - 1:
                self.frame_index = 0
            else:
                self.frame_index += 1
            self.set_texture(self.frame_index)