from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.vector import Vector
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy import Config
from kivy.uix.boxlayout import BoxLayout

__author__ = 'D4rkFr4g'

class SlideTile(Widget):
    is_touched = False

    def on_touch_down(self, touch):
        #print str(self.id)
        if self.collide_point(touch.x, touch.y):
            self.is_touched = True

    def on_touch_move(self, touch):
        if self.is_touched:
            #print self.pos
            self.center = touch.pos

    def on_touch_up(self, touch):
        print 'Dirty Touch'
        self.is_touched = False


class SliderGame(Widget):
    texture = ObjectProperty()

    def __init__(self, **kwargs):
        super(SliderGame, self).__init__(**kwargs)
        self.texture = Image(source='images/puzzle.png').texture


class SpaceSliderApp(App):
    def build(self):
        game = SliderGame()
        return game


if __name__ == '__main__':
    # Set Window to fullscreen
    #Config.set('graphics', 'fullscreen', 'auto')
    #Config.write()

    SpaceSliderApp().run()


    # As requested by Aselus
    wedding_description = ("The wedding was actually kinda boring. There was an off-tempo bongo/n"
                           "drummer during the service. They made us wait too long for food/n"
                           "but there was a whole pig to eat./n")
    #print wedding_description