from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.uix.behaviors import DragBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty, ObjectProperty, BooleanProperty, ListProperty, ReferenceListProperty
import numpy as np
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.graphics import Line, Rectangle, Color
from kivy.vector import Vector
from random import randint
#TESTE
class TelaPrincipal(Screen):

    # Set main variables
    ball = ObjectProperty(None)
    ballClicked = BooleanProperty(False)
    rays = ListProperty()
    obstacles = ListProperty()

    # Set number of rays and obstacles
    nRays = NumericProperty(100)
    nObstacles = NumericProperty(5)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        Clock.schedule_interval(self.update,0.01/60.0)
        
        # Add obstacles
        for i in range(self.nObstacles):
            self.obstacle = Obstacle()
            self.obstacle.pos = [randint(0,self.width-100),randint(0,self.height-100)]
            self.obstacles.append(self.obstacle)
            self.ids.obstacleLayout.add_widget(self.obstacle)

        # Add rays
        for i in range(self.nRays):
            self.ray = Ray(angle=i*360.0/self.nRays, center=Window.center)
            self.rays.append(self.ray)
            self.add_widget(self.ray)
        
        


    def on_touch_down(self, touch):
        if self.ball.collide_point(*touch.pos):
            self.ballClicked = True
        return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        self.ballClicked = False
        return super().on_touch_up(touch)

    def on_touch_move(self, touch):
        if self.ballClicked == True:
            self.ball.center = touch.pos
            
            
        return super().on_touch_move(touch)

    def update(self, dt):
        for raio in self.rays:
            raio.center = self.ball.center
            raio.ShootRays(obstacles=self.obstacles)
        
        for obs in self.obstacles:
            obs.redraw()

class Ball(Widget):
    pass 

class Obstacle(Widget):
    
    def redraw(self):
        self.canvas.clear()
        with self.canvas:
            Color(rgba= (1,0,0,0.1))
            Rectangle(pos=self.pos, size=self.size, width=5)
            #Line(width= 1, rectangle= (self.pos[0],self.pos[1],self.width,self.height))
    
    
class Ray(Widget):
    def __init__ (self, angle, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.angle = angle
        self.size_hint = (None,None)        
    
    def ShootRays(self, obstacles):
        addValue = 10

        #vectMov = Vector(addValue,addValue).rotate(self.angle)

        #vectMov_x = np.sin(np.radians(self.angle))
        #vectMov_y = np.cos(np.radians(self.angle))

        finalPos_x = self.center_x
        finalPos_y = self.center_y
        finalPos = [finalPos_x,finalPos_y]
        obstaclesList = obstacles

        # outObstRegionList = ListProperty()
        # for obst in obstaclesList:
        #     outObstRegion = OutRegion(center= obst.center, )


        #self.parent.add_widget(outObstRegion)

        hit = False
        while not hit:

            vectMov = Vector(addValue,addValue).rotate(self.angle)
            finalPos_x += vectMov.x
            finalPos_y += vectMov.y
            #finalPos_x += vectMov_x
            #finalPos_y += vectMov_y

            if finalPos_x <= 0 or finalPos_x >= self.parent.width:
                hit = True

            if finalPos_y <=0 or finalPos_y >= self.parent.height:
                hit = True

            for obstacle in obstaclesList:
                # if obstacle.collide_point(finalPos_x, finalPos_y):
                #     hit=True
                #     print(finalPos_x, obstacle.right,obstacle.pos[0],finalPos_y,obstacle.pos[1],obstacle.top)
               # print()

                # if finalPos_x <= obstacle.right+11 and finalPos_x >= obstacle.pos[0]-11 and finalPos_y >= obstacle.pos[1]-11 and finalPos_y <= obstacle.top+11:
                #     addValue=2

                if finalPos_x <= obstacle.right+addValue+1 and finalPos_x >= obstacle.pos[0]-addValue-1 and finalPos_y >= obstacle.pos[1]-addValue-1 and finalPos_y <= obstacle.top+addValue+1:
                    addValue = 1
                    
                

                if finalPos_x <= obstacle.right and finalPos_x >= obstacle.pos[0] and finalPos_y >= obstacle.pos[1] and finalPos_y <= obstacle.top:
                    hit=True


                
                


        self.canvas.clear()
        with self.canvas:
            
            #Color(rgba=[1,0.1,0.5,0.2])
            #Rectangle(pos=self.pos, size=self.size)
            Color(rgba=[1,1,1,1])
            Line(points=[self.center_x, self.center_y, finalPos_x, finalPos_y], width = 1)
    
class OutRegion(Widget):
    pass

class RT2D_App(App):
    def build(self):
        tela = TelaPrincipal()
        #Clock.schedule_interval(tela.update,1.0/60.0)
        return tela

app = RT2D_App()
app.run()
        
    