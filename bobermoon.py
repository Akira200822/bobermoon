import arcade
import random

import animate

SCREEN_WIDTH=660
SCREEN_HEIGHT=660
SCREEN_TITLE="Bomberman"
CELL_WIDTH=60
CELL_HEIGHT=60
ROW_COUNT=11
COLUMN_COUNT=11

class Bomberman(animate.Animation):
    def __init__(self):
        super().__init__("Bomberman/Front/Bman_F_f00.png", 0.5)
        self.walk_down_frames=[]
        for i in range(8):
            self.walk_down_frames.append(arcade.load_texture(f"Bomberman/Front/Bman_F_f0{i}.png"))
        self.walk_up_frames=[]
        for i in range(8):
            self.walk_up_frames.append(arcade.load_texture(f"Bomberman/Back/Bman_B_f0{i}.png"))
        self.walk_right_frames=[]
        for i in range(8):
            self.walk_right_frames.append(arcade.load_texture(f"Bomberman/Side/Bman_S_f0{i}.png"))
        self.walk_left_frames=[]
        for i in range(8):
            self.walk_left_frames.append(arcade.load_texture(f"Bomberman/Side/Bman_S_f0{i}.png",
                                                             flipped_horizontally=True))

        self.direction=4

    def costume_change(self):
        if self.direction==1:
            self.textures=self.walk_left_frames
        if self.direction==2:
            self.textures = self.walk_right_frames
        if self.direction==3:
            self.textures=self.walk_up_frames
        if self.direction==4:
            self.textures = self.walk_down_frames



class ExplodableBlock(arcade.Sprite):
    def __init__(self):
        super().__init__("Blocks/ExplodableBlock.png", 1)


class Solid_block(arcade.Sprite):
    def __init__(self):
        super().__init__("Blocks/SolidBlock.png")

class Game(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width, height, title)
        self.back=arcade.load_texture("Blocks/BackgroundTile.png")

        self.solid_blocks = arcade.SpriteList()
        self.explodable_blocks =arcade.SpriteList()
        self.bomberman=Bomberman()


    def difference(self, coordinate, distance):
        return coordinate*distance+distance/2

    def setup(self):
        for y in range(ROW_COUNT):
            for x in range(COLUMN_COUNT):
                if x%2==1 and y%2==1:
                    solid_block=Solid_block()
                    solid_block.center_x = self.difference(x, CELL_WIDTH)
                    solid_block.center_y = self.difference(y, CELL_HEIGHT)
                    self.solid_blocks.append(solid_block)
                elif random.randint(1,2)==1:
                    if (not (x==0 and y<=2) and not (y==0 and x <=2)
                            and not(x==ROW_COUNT-1 and y>=COLUMN_COUNT-3)
                            and not (y==COLUMN_COUNT-1 and x>=ROW_COUNT-3)):
                        explodable_block=ExplodableBlock()
                        explodable_block.center_x = self.difference(x, CELL_WIDTH)
                        explodable_block.center_y = self.difference(y, CELL_HEIGHT)
                        self.explodable_blocks.append(explodable_block)

        x=SCREEN_WIDTH/COLUMN_COUNT-CELL_WIDTH/2
        y=SCREEN_HEIGHT/ROW_COUNT-CELL_HEIGHT/2
        self.bomberman.set_position(x,y)



    def on_draw(self):
        self.clear()
        for y in range(ROW_COUNT):
            for x in range(COLUMN_COUNT):
                arcade.draw_texture_rectangle(
                    self.difference(x, CELL_WIDTH),
                    self.difference(y, CELL_HEIGHT),
                    CELL_WIDTH, CELL_HEIGHT,
                    self.back)
        self.solid_blocks.draw()
        self.explodable_blocks.draw()
        self.bomberman.draw()




    def update(self, delta_time):
        self.bomberman.update_animation(delta_time)

    def on_key_press(self, key, modifiers):
        if key==arcade.key.LEFT:
            self.bomberman.direction=1
        if key==arcade.key.RIGHT:
            self.bomberman.direction=2
        if key==arcade.key.UP:
            self.bomberman.direction=3
        if key==arcade.key.DOWN:
            self.bomberman.direction=4
        self.bomberman.costume_change()


    def on_key_release(self, key, modifiers):
        pass


window=Game(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
window.setup()
arcade.run()