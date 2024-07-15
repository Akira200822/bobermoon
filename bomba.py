import animate
import arcade
import time



class Bomba(animate.Animation):
    def __init__(self):
        super().__init__("Bomb/Bomb_f00.png", 0.7)
        self.bomb_timer = time.time()

        for i in range(3):
            self.append_texture(arcade.load_texture(f"Bomb/Bomb_f0{i}.png"))