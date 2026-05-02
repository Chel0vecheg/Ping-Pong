from pygame import *
from random import randint

font.init()
font1 = font.SysFont('Arial', 40)
player1_win = font1.render('Player1 WON!', True, (0, 0, 0))
player2_win = font1.render('Player2 WON!', True, (0, 0, 0))


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

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 140:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 140:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self,player_image, player_x, player_y, size_x, size_y, player_speed,speed_y,speed_x,):
        super().__init__(player_image, player_x, player_y, size_x, size_y, player_speed)
        self.speed_y = speed_y
        self.speed_x = speed_x
    def move(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        if self.rect.y < -18 or self.rect.y > 470:
            self.speed_y*=-1
        

        

ball = Ball('PingPongBall.png',150,150,50,50,0,3,3)
P1 = Player('PalkaV3.png',50,150,30,140,7)
P2 = Player('PalkaV3.png',625,150,30,140,7)

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
        P1.reset()
        P1.update_l()
        P2.reset()
        P2.update_r()
        ball.reset()
        ball.move()
        if sprite.collide_rect(ball, P2) or sprite.collide_rect(ball, P1):
            ball.speed_x *= -1
            random = randint(1,2)
            if random == 1:
                random2 = randint(1,3)
                if random2 == 1:
                    ball.speed_x += 1
                if random2 == 2:
                    ball.speed_x += 2
                if random2 == 3:
                    ball.speed_x += 3
            elif random == 2 and ball.speed_x < 1:
                ball.speed_x -= 1
        if ball.rect.x <= 0:
            window.blit(player2_win, (225, 200))
            finish = True
        elif ball.rect.x >= 650:
            window.blit(player1_win, (225,200))
            finish = True
        display.update()
    clock.tick(60)
