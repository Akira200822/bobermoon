import arcade
import animate
import time


class Explosion(animate.Animation):
    def __init__(self):
        super().__init__("Flame/Flame_f00.png", 0.7)
        self.explosion_timer=time.time()

    def update(self):
        if time.time() - self.explosion_timer>2:
            self.kill()
