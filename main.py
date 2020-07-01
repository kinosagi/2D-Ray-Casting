from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.uix.behaviors import DragBehavior
from kivy.properties import NumericProperty
import numpy as np
from kivy.core.window import Window

class TelaPrincipal(Screen):
    pass

class Ball(DragBehavior,Widget):
    
    def buildRays(self):
        ray = Ray(30)
        self.add_widget(ray)
    
    def on_touch_move(self, touch):
        
        if self.collide_point(*touch.pos):
            self.buildRays()
        return super().on_touch_move(touch)

class Ray(Widget):
    def __init__ (self, angle, **kwargs):
        super().__init__(**kwargs)
        angle = NumericProperty(angle)
        print(angle)

class RT2D_App(App):

    def build(self):
        return TelaPrincipal()

app = RT2D_App()
app.run()
        
    