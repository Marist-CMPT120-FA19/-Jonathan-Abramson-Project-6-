#Jonathan Abramson
#Traffic Light using Functions
#New and improved

from graphics import *

win= GraphWin("Traffic_light", 225, 225)

def draw_light_body(x, y, length, width):
    body=Rectangle (Point(x,y), Point(length, width))
    body.setFill("light goldenrod yellow")
    body.setOutline("black")
    body.draw(win)
#draws body of the light

def draw_lamp(color, a, b, radius):
    lamp = Circle(Point(a,b), radius)
    lamp.setFill(color)
    lamp.setOutline("black")
    lamp.draw(win)
#Tells the code how to draw the lamps

def draw_traffic_light(x, y):
    draw_light_body(x,y,75,155)
    draw_lamp("red", 50,30,10)
    draw_lamp("yellow", 50,80,10)
    draw_lamp("green", 50, 130, 10)
#Provides coordinates of the different lamps and the lamp body

draw_traffic_light(25,5)

win.getMouse() # pause for click in window
