import arcade
import random

import player
from exp_block import ExplodableBlock
from solid_block import Solid_block

import constants

class Game(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width, height, title)
        self.back=arcade.load_texture("Blocks/BackgroundTile.png")

        self.solid_blocks = arcade.SpriteList()
        self.explodable_blocks =arcade.SpriteList()

        self.bomberman = player.Bomberman(constants.PLAYER_ONE_SPEED)
        self.bomberman_two = player.Bomberman(constants.PLAYER_TWO_SPEED)
        self.bomberman_two.color = (0, 247, 234)

    def difference(self, coordinate, distance):
        return coordinate*distance+distance/2

    def setup(self):
        for y in range(constants.ROW_COUNT):
            for x in range(constants.COLUMN_COUNT):
                if x%2==1 and y%2==1:
                    solid_block=Solid_block()
                    solid_block.center_x = self.difference(x, constants.CELL_WIDTH)
                    solid_block.center_y = self.difference(y, constants.CELL_HEIGHT)
                    self.solid_blocks.append(solid_block)
                elif random.randint(1,2)==1:
                    if (not (x==0 and y<=2) and not (y==0 and x <=2)
                            and not(x==constants.ROW_COUNT-1 and y>=constants.COLUMN_COUNT-3)
                            and not (y==constants.COLUMN_COUNT-1 and x>=constants.ROW_COUNT-3)):
                        explodable_block=ExplodableBlock()
                        explodable_block.center_x = self.difference(x, constants.CELL_WIDTH)
                        explodable_block.center_y = self.difference(y, constants.CELL_HEIGHT)
                        self.explodable_blocks.append(explodable_block)

        x=constants.SCREEN_WIDTH/constants.COLUMN_COUNT-constants.CELL_WIDTH/2
        y=constants.SCREEN_HEIGHT/constants.ROW_COUNT-constants.CELL_HEIGHT/2
        self.bomberman.set_position(x,y)

        x = constants.SCREEN_WIDTH-constants.ROW_COUNT*2
        y = constants.SCREEN_HEIGHT-constants.CELL_HEIGHT+constants.ROW_COUNT*3
        self.bomberman_two.set_position(x, y)

    def on_draw(self):
        self.clear()
        for y in range(constants.ROW_COUNT):
            for x in range(constants.COLUMN_COUNT):
                arcade.draw_texture_rectangle(
                    self.difference(x, constants.CELL_WIDTH),
                    self.difference(y, constants.CELL_HEIGHT),
                    constants.CELL_WIDTH, constants.CELL_HEIGHT,
                    self.back)
        self.solid_blocks.draw()
        self.explodable_blocks.draw()
        self.bomberman.draw()
        self.bomberman_two.draw()

    def update(self, delta_time):
        self.bomberman.update_animation(delta_time)
        self.bomberman_two.update_animation(delta_time)
        self.bomberman.update()
        self.bomberman_two.update()

    def on_key_press(self, key, modifiers):
        if key==arcade.key.LEFT:
            self.bomberman.to_left()
        if key==arcade.key.RIGHT:
            self.bomberman.to_right()
        if key==arcade.key.UP:
            self.bomberman.to_up()
        if key==arcade.key.DOWN:
            self.bomberman.to_down()
        self.bomberman.costume_change()

        if key==arcade.key.A:
            self.bomberman_two.to_left()
        if key==arcade.key.D:
            self.bomberman_two.to_right()
        if key==arcade.key.W:
            self.bomberman_two.to_up()
        if key==arcade.key.S:
            self.bomberman_two.to_down()
        self.bomberman_two.costume_change()

    def on_key_release(self, key, modifiers):
        if (key == arcade.key.LEFT or key == arcade.key.RIGHT or
                key == arcade.key.UP or key == arcade.key.DOWN):
            self.bomberman.to_stop()

        if (key == arcade.key.A or key == arcade.key.D or
                key == arcade.key.W or key == arcade.key.S):
            self.bomberman_two.to_stop()

window=Game(constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT,constants.SCREEN_TITLE)
window.setup()
arcade.run()