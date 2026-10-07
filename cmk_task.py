from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')

tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
update_canvas()
delay(2)
close_canvas()