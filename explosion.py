import arcade
import animate


class Explosion(animate.Animation):
    def __init__(self):
        super().__init__("Flame/Flame_f00.png", 0.7)
