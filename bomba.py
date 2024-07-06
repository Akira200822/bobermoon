import animate
import arcade

class Bomb(animate.Animation):
    def __init__(self):
        super().__init__("Bomb/Bomb_f00.png",0.7)

        for i in range(3):
            self.append_texture(arcade.load_texture(f"Bomb/Bomb_f0{i}.png"))

