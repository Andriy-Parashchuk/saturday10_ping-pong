from pygame import *
font.init()


class GameSprite(sprite.Sprite):
    """
    main class for future objects
    """
    def __init__(self, sprite_image, x, y, width, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        virtual_surface.blit(self.image, (self.rect.x, self.rect.y))


class Ball(GameSprite):
    """
    class for create ball object
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__("ball.png", x, y, 50, 50, 10)
        self.speed_x = self.speed
        self.speed_y = self.speed

    def update(self):
        global score_left
        global score_right
        global text_score_left
        global text_score_right

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.y >= HEIGHT - self.rect.width:
            self.speed_y *= -1

        if self.rect.y <= 0:
            self.speed_y *= -1

        if self.rect.colliderect(platform_left.rect) or self.rect.colliderect(platform_right.rect):
            self.speed_x *= -1

        if self.rect.x >= WIDTH:
            score_left += 1
            text_score_left = font_interface.render(str(score_left), True, (0, 0, 0))
            self.rect.x = self.x
            self.rect.y = self.y

        if self.rect.x <= 0:
            score_right += 1
            text_score_right = font_interface.render(str(score_right), True, (0, 0, 0))
            self.rect.x = self.x
            self.rect.y = self.y


class Platform(GameSprite):
    """
    class for create platform object
    """
    def __init__(self, x, y, angle, player):
        super().__init__("platform.png", x, y, 150, 20, 10)
        self.image = transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.player = player

    def update(self):
        keys_pressed = key.get_pressed()

        if self.player == 1:
            if keys_pressed[K_w] and self.rect.y > 5:
                self.rect.y -= self.speed
            if keys_pressed[K_s] and self.rect.y < HEIGHT - self.rect.height:
                self.rect.y += self.speed

        if self.player == 2:
            if keys_pressed[K_UP] and self.rect.y > 5:
                self.rect.y -= self.speed
            if keys_pressed[K_DOWN] and self.rect.y < HEIGHT - self.rect.height:
                self.rect.y += self.speed


WIDTH = 1200
HEIGHT = 700

ASPECT_RATIO = WIDTH / HEIGHT

clock = time.Clock()
fps = 60

back = (106, 245, 168)

window = display.set_mode((WIDTH, HEIGHT), RESIZABLE)
display.set_caption("Ping-pong")

virtual_surface = Surface((WIDTH, HEIGHT))
virtual_surface.fill(back)
current_size = window.get_size()

game = True

ball = Ball(575, 375)

platform_left = Platform(150, 300, -90, 1)
platform_right = Platform(1050, 300, 90, 2)

score_left = 0
score_right = 0

font_interface = font.Font(None, 60)

text_score_left = font_interface.render(str(score_left), True, (0, 0, 0))
text_score_right = font_interface.render(str(score_right), True, (0, 0, 0))


"""
main loop for game
"""
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                game = False
        if e.type == VIDEORESIZE:
            new_width = e.w
            new_height = int(new_width / ASPECT_RATIO)
            window = display.set_mode((new_width, new_height), RESIZABLE)
            current_size = window.get_size()

    virtual_surface.fill(back)

    ball.update()
    ball.reset()

    platform_left.update()
    platform_left.reset()

    platform_right.update()
    platform_right.reset()

    virtual_surface.blit(text_score_left, (550, 20))
    virtual_surface.blit(text_score_right, (650, 20))

    scaled_surface = transform.scale(virtual_surface, current_size)
    window.blit(scaled_surface, (0, 0))
    display.update()
    clock.tick(fps)
