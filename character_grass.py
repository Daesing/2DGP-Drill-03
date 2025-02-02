from pico2d import *
import math

open_canvas()


grass = load_image('grass.png')
character = load_image('character.png')

# fill here
def draw_boy(x,y):
    clear_canvas_now()
    character.draw_now(x,y)
    delay(0.1)


def run_top():
    print('TOP')
    for x in range(0,800,10):
        draw_boy(x,550)
    pass

def run_right():
    print('RIGHT')
    for y in range(550,0,-10):
        draw_boy(790, y)
    pass

def run_bottom():
    print('bottom')
    for x in range(800,0,-10):
        draw_boy(x, 0)
    
    pass

def run_left():
    print('left')
    for y in range(0,550,10):
        draw_boy(0, y)
    
    pass


def run_rect():
    print('rect')

    run_top()
    run_right()
    run_bottom()
    run_left()

    pass

def run_circle():
    print('circle')


    r, cx, cy  = 300, 800//2, 600//2
    

    for degree in range(0, 360, 3):
        theta = math.radians(degree)
        x = r * math.cos(theta) + cx
        y = r * math.sin(theta) + cy

        draw_boy(x,y)
    
    pass


def draw_bottom():
    for x in range(0,790,10):
        draw_boy(x, 0)
    pass

def draw_right():
    for y in range(0,550,10):
        draw_boy(790, y)
    pass

def draw_side():
    x,y=790,550
    while x!=0 and y!=0:    
        draw_boy(x, y)
        x=x-15
        y=y-10
    pass

def run_triangle():
    draw_bottom()
    draw_right()
    draw_side()
    pass


while True:
    run_circle()
    run_rect()
    run_triangle()
    delay(0.1)



 
close_canvas()
