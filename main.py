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

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            self.is_touched = True
            print 'tile_id = ' + str(self.tile_id)

    def on_touch_move(self, touch):
        if self.is_touched:
            #print self.pos
            self.center = touch.pos

    def on_touch_up(self, touch):
        if self.is_touched:
            #print 'Dirty Touch'
            self.is_touched = False
            SliderGame.reposition_tiles(SpaceSliderApp.game)


class SliderGame(Widget):
    #texture = Image(source='images/puzzle.png').texture
    my_image = 'images/puzzle.png'
    texture = ObjectProperty()
    #tile_list = [[i] for i in range(16)]
    tile_list = []
    grid_pos = []
    num_of_tiles = 16

    def __init__(self, **kwargs):
        super(SliderGame, self).__init__(**kwargs)
        self.texture = Image(source='images/puzzle.png').texture

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
        #print 'screen_width = ' + str(self.parent.width / 2.0)
        #start_x = (self.width / 2.0) - (tile_width * 2)
        #start_y = (self.height / 2.0) + (tile_height * 2)
        start_x = 200
        start_y = 400
        current_pos = start_x, start_y

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
        # game = SliderGame()
        # game.init_tiles()
        # #game.texture_tiles()
        # game.shuffle_tiles()
        # game.print_tiles()

        self.game = SliderGame()
        self.game.init_tiles()
        self.game.shuffle_tiles()
        self.game.print_tiles()


        #return game
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