from pico2d import *
import math

open_canvas()


grass = load_image('grass.png')
character = load_image('character.png')

# fill here

def run_top():
    print('TOP')
    pass

def run_right():
    print('RIGHT')
    pass

def run_bottom():
    print('bottom')
    pass

def run_left():
    print('left')
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

        clear_canvas_now()
        character.draw_now(x,y)
        delay(0.1)

    pass



while True:
    # run_circle()
    run_rect()
    break

'''
while True:
    user_input=input("Enter q to quit: ")
    if user_input.lower()=="q":
        break
        '''
        



 
close_canvas()
