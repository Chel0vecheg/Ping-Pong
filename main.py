from pygame import *
from random import randint

#*font.init()
#*font1 = font.SysFont('Arial', 80)
#*player1_win = font1.render('Player1 WON!', True, (0, 0, 0))
#*player2_win = font1.render('Player2 WON!', True, (0, 0, 0))
#*font2 = font.SysFont('Arial', 36)

#! 
#* 
#? 
#//

#?фоновая музыка
#?mixer.init()
#?mixer.music.load('space.ogg')
#?mixer.music.play()
#?fire_sound = mixer.Sound('fire.ogg')

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#!
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 70:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 70:
            self.rect.y += self.speed
#!

ball = GameSprite('PingPongBall.png',150,150,50,50,0)

win_width = 700
win_height = 500
display.set_caption("Ping Pong")
window = display.set_mode((win_width, win_height))
#//background = transform.scale(image.load(img_back), (win_width, win_height))
background = (100, 149, 237)
clock = time.Clock()

finish = False

run = True 
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        window.fill(background)
        ball.reset()
        display.update()
    clock.tick(60)
