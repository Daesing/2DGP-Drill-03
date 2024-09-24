from pico2d import *

open_canvas()


grass = load_image('grass.png')
character = load_image('character.png')

# fill here

def run_rect():
    print('rect')
    pass
def run_circle():
    print('circle')

    clear_canvas_now()
    character.draw_now(400,300)
    delay(0.1)
    pass

while True:
    run_rect()
    run_circle()
    break


while True:
    user_input=input("Enter q to quit: ")
    if user_input.lower()=="q":
        break
        
        



 
close_canvas()
