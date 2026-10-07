from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
SPEED = 10

def handle_events():
    global running, dx, dy
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dx += 1
            elif event.key == SDLK_LEFT:
                dx -= 1
            elif event.key == SDLK_UP:
                dy += 1
            elif event.key == SDLK_DOWN:
                dy -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dx -= 1
            elif event.key == SDLK_LEFT:
                dx += 1
            elif event.key == SDLK_UP:
                dy -= 1
            elif event.key == SDLK_DOWN:
                dy += 1

open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
dx, dy = 0, 0
face = 1

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    if dx != 0:
        face = 1 if dx > 0 else -1

    if dx == 0 and dy == 0:
        row = 300 if face == 1 else 200
    else:
        row = 100 if face == 1 else 0

    character.clip_draw(frame * 100, row, 100, 100, x, y)
    update_canvas()
    handle_events()
    x += dx * SPEED
    y += dy * SPEED
    frame = (frame + 1) % 8
    delay(0.05)
close_canvas()