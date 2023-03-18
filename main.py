from pygame import *

WIDTH = 1200
HEIGHT = 700

clock = time.Clock()
fps = 60

back = (106, 245, 168)

window = display.set_mode((WIDTH, HEIGHT), RESIZABLE)
window.fill(back)
display.set_caption("Ping-pong")

game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                game = False

    window.fill(back)
    display.update()
    clock.tick(fps)
