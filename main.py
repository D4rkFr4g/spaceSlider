from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy import Config
from random import shuffle
import math

__author__ = 'D4rkFr4g'


class SlideTile(Widget):
    is_touched = False
    blank_tile_index = 0
    current_tile_index = 0
    blank_grid_pos = 0, 0
    current_grid_pos = 0, 0

    @staticmethod
    def reposition():
        SliderGame.reposition_tiles(SpaceSliderApp.game)

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            self.is_touched = True
            self.find_tile_positions()
            print 'tile_id = ' + str(self.tile_id)

    def find_tile_positions(self):
        game = SpaceSliderApp.game

        # Store position of current and blank tile index
        for i in range(0, game.num_of_tiles):
            if game.tile_list[i].tile_id == 12:
                self.blank_tile_index = i

            if game.tile_list[i].tile_id == self.tile_id:
                self.current_tile_index = i

        current_row = (self.current_tile_index) / 4
        current_col = self.current_tile_index % 4
        self.current_grid_pos = current_row, current_col

        blank_row = (self.blank_tile_index) / 4
        blank_col = self.blank_tile_index % 4
        self.blank_grid_pos = blank_row, blank_col

        #print 'current_row = ' + str(self.current_grid_pos[0])
        #print 'current_col = ' + str(self.current_grid_pos[1])
        #print 'blank_row = ' + str(self.blank_grid_pos[0])
        #print 'blank_col = ' + str(self.blank_grid_pos[1])

    def on_touch_move(self, touch):
        if self.is_touched:
            #print self.pos
            self.move_tiles(touch)
            #self.center = touch.pos

    def on_touch_up(self, touch):
        if self.is_touched:
            #print 'Dirty Touch'
            self.is_touched = False
            self.reposition()

    def move_tiles(self, touch):

        # Figure out direction of blank space tile_id == 12

        # Figure which direction user is trying to go
        move_vector = touch.pos[0] - self.center_x, touch.pos[1] - self.center_y
        if abs(move_vector[0]) > abs(move_vector[1]):
            # Moving x_direction
            if self.current_grid_pos[0] == self.blank_grid_pos[0]:
                # Same Row as blank
                if abs(self.current_grid_pos[1] - self.blank_grid_pos[1]) == 1:
                    # Next to blank
                    if (move_vector[0] > 0 and self.blank_grid_pos[1] > self.current_grid_pos[1]) or (
                            move_vector[0] < 0 and self.blank_grid_pos[1] < self.current_grid_pos[1]):
                        # Towards blank
                        self.set_center_x(touch.pos[0])
        else:
            # Moving y_direction
            if self.current_grid_pos[1] == self.blank_grid_pos[1]:
                # Same Col as blank
                if abs(self.current_grid_pos[0] - self.blank_grid_pos[0]) == 1:
                    # Next to blank
                    if (move_vector[1] < 0 and self.blank_grid_pos[0] > self.current_grid_pos[0]) or (
                            move_vector[1] > 0 and self.blank_grid_pos[0] < self.current_grid_pos[0]):
                        # Towards blank
                        self.set_center_y(touch.pos[1])

        # Readjust the grid according to the new order. ?New World Order?




class SliderGame(Widget):
    my_image = 'images/puzzle.png'
    texture = ObjectProperty()
    tile_list = []
    grid_pos = []
    num_of_tiles = 16
    blank_id = 12

    def __init__(self, **kwargs):
        super(SliderGame, self).__init__(**kwargs)

    def texture_tiles(self):
        print 'Now texturing tiles'
        # Divide up the image texture to fit on all the squares
        num_of_cols = int(math.sqrt(self.num_of_tiles))
        num_of_rows = num_of_cols
        grid_pos = []

        width = self.texture.width / num_of_cols
        height = self.texture.height / num_of_cols

        x, y = 0, height * (num_of_cols  - 1)
        k = 0
        for i in range(0, num_of_rows):
            for j in range(0, num_of_cols):
                print '[' + str(x) + ', ' + str(y) + ', ' + str(width) + ', ' + str(height) + ']'
                self.tile_list[k].texture = self.texture.get_region(x, y, width, height)
                k += 1
                x += width

            x = 0
            y -= height

    def init_tiles(self):

        tile_width = self.width
        tile_height = self.height
        start_x = 200
        start_y = 400
        current_pos = start_x, start_y

        # Setup all the tile positions in the grid
        for i in range(0, 4):
            for j in range(0, 4):
                pos = current_pos
                self.grid_pos.append(pos)
                #print pos

                # Move to the next x position
                current_pos = current_pos[0] + tile_width, current_pos[1]

            # Move to the next y position
            current_pos = start_x, current_pos[1] - tile_height

        i = 0
        x, y = 50, 50
        while i < self.num_of_tiles:
            temp = SlideTile()
            temp.tile_id = i
            temp.size = self.width * 1, self.height * 1
            temp.pos = self.grid_pos[i]
            my_image = temp.ids['my_image']
            my_image.source = 'images/puzzle_' + str(i) + '.png'   # For testing purposes
            self.tile_list.append(temp)     # Add to window
            self.add_widget(temp)
            i += 1

    def reposition_tiles(self):
        for i in range(0, self.num_of_tiles):
            self.tile_list[i].pos = self.grid_pos[i]

    def shuffle_tiles(self):
        shuffle(self.tile_list)
        self.reposition_tiles()

    def print_tiles(self):
        i = 0
        print '[',
        while i < self.num_of_tiles - 1:
            print str(self.tile_list[i].tile_id) + ', ',
            i += 1

        print str(self.tile_list[15].tile_id) + ']'


class SpaceSliderApp(App):
    game = SliderGame()

    def build(self):
        self.game = SliderGame()
        self.game.init_tiles()
        self.game.shuffle_tiles()
        self.game.print_tiles()

        return self.game


if __name__ == '__main__':
    # Set Window to fullscreen
    #Config.set('graphics', 'fullscreen', 'no')
    #Config.write()

    SpaceSliderApp().run()


    # As requested by Aselus
    wedding_description = ("The wedding was actually kinda boring. There was an off-tempo bongo/n"
                           "drummer during the service. They made us wait too long for food/n"
                           "but there was a whole pig to eat./n")
    #print wedding_description