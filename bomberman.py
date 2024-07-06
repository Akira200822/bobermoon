import arcade
import animate
import constants


class Bomberman(animate.Animation):
    def __init__(self, speed):
        super().__init__("Bomberman/Front/Bman_F_f00.png", 0.5)
        self.speed = speed
        self.walk_down_frames = []
        for i in range(8):
            self.walk_down_frames.append(
                arcade.load_texture(f"Bomberman/Front/Bman_F_f0{i}.png")
            )
        self.walk_up_frames = []
        for i in range(8):
            self.walk_up_frames.append(
                arcade.load_texture(f"Bomberman/Back/Bman_B_f0{i}.png")
            )
        self.walk_right_frames = []
        for i in range(8):
            self.walk_right_frames.append(
                arcade.load_texture(f"Bomberman/Side/Bman_S_f0{i}.png")
            )
        self.walk_left_frames = []
        for i in range(8):
            self.walk_left_frames.append(
                arcade.load_texture(
                    f"Bomberman/Side/Bman_S_f0{i}.png", flipped_horizontally=True
                )
            )

        self.direction = 4
        self.motion = 0

    def to_up(self):
        if not self.motion:
            self.motion = 1
            self.direction = 3
            self.change_y = self.speed

    def to_down(self):
        if not self.motion:
            self.motion = 1
            self.direction = 4
            self.change_y = -self.speed

    def to_left(self):
        if not self.motion:
            self.motion = 1
            self.direction = 1
            self.change_x = -self.speed

    def to_right(self):
        if not self.motion:
            self.motion = 1
            self.direction = 2
            self.change_x = self.speed

    def to_stop(self):
        self.change_x = 0
        self.change_y = 0
        self.motion = 0

    def costume_change(self):
        if self.direction == 1:
            self.textures = self.walk_left_frames
        if self.direction == 2:
            self.textures = self.walk_right_frames
        if self.direction == 3:
            self.textures = self.walk_up_frames
        if self.direction == 4:
            self.textures = self.walk_down_frames

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        if self.right > constants.SCREEN_WIDTH:
            self.right = constants.SCREEN_WIDTH
        if self.bottom < 0:
            self.bottom = 0
        if self.top > constants.SCREEN_HEIGHT:
            self.top = constants.SCREEN_HEIGHT
