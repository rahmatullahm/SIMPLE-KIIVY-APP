from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import NumericProperty
from random import choice, randint
class MainBoard(Widget):
    speed = 0
    xx = None
    yy = None
    ax = [-3,-2,-1,1,2,3]
    ay = [-3,-2,-1,1,2,3] 
    score_r = NumericProperty(0)
    score_l = NumericProperty(0)
    def __init__(self, **kwargs):
        super(MainBoard, self).__init__(**kwargs)
        self.myball = self.ball
        self.serve_ball()
        
    def update(self, dt):
        self.crush_border()
        self.crush_paddles()
        self.move(self.xx, self.yy)
    def move(self, xx, yy):
        self.myball.x  += xx
        self.myball.y += yy
    def crush_border(self):
        if self.myball.collide_widget(self.r_side):
            self.xx = -self.xx
            self.score_l +=1
            self.serve_ball()
        if self.myball.collide_widget(self.l_side):
            self.xx = -self.xx
            self.score_r +=1
            self.serve_ball()
        if self.myball.collide_widget(self.tops):
            self.yy = -self.yy
        if self.myball.collide_widget(self.bottom):
            self.yy = -self.yy
    def crush_paddles(self):
        if self.myball.collide_widget(self.r_paddle):
            self.xx = -self.xx
            self.xx += .3
            self.yy -= .3
        if self.myball.collide_widget(self.l_paddle):
            self.xx = -self.xx
            self.xx -= .3
            self.yy += .3
    def on_touch_move(self, touch):
        if touch.x < 80:
            if touch.y >self.r_paddle.height/2 + 10 and touch.y < self.height - self.r_paddle.height/2 - 10:
                self.r_paddle.center_y = touch.y
        if touch.x > self.width -80:
            if touch.y >self.l_paddle.height/2 + 10 and touch.y < self.height - self.l_paddle.height/2 - 10:
                self.l_paddle.center_y= touch.y
    def serve_ball(self):
        self.myball.center = self.center
        self.xx = choice(self.ax)
        self.yy = choice(self.ay)
class Side(Widget):
    pass

class Top_Bottom(Widget):
    pass

class Ball(Widget):
    pass
class Paddle(Widget):
    pass
class GameApp(App):
    def build(self):
        game = MainBoard()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game

GameApp().run()