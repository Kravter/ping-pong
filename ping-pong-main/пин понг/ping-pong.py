from pygame import *
from random import randint
from time import time as timer

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 1:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed

game = True
finish = False
window = display.set_mode((700, 500))
window.fill((4, 245, 126))
player1 = Player("test_platf.png", 100, 300, 10, 100, 3)
player2 = Player("test_platf.png", 600, 300, 10, 100, 3)
balls = GameSprite("asteroid.png", 340, 120, 60, 60, 1 )
font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('plater 1 lose', True, (180, 0 ,0))
lose2 = font1.render('plater 2 lose', True, (180, 0 ,0))

FPS = 120
clock = time.Clock()
speed_x = 3
speed_y = 3
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill((4, 245, 126))
        balls.rect.x += speed_x
        balls.rect.y += speed_y
        player2.update_l()
        
        balls.reset()
        player1.update_r()
        player1.reset()
        player2.reset()
    if balls.rect.y > 450 or balls.rect.y < 0:
        speed_y *=-1

    if sprite.collide_rect(balls, player1) or sprite.collide_rect(balls, player2):
        speed_x *=-1
    if balls.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))   
    if balls.rect.x > 700:
        finish = True
        window.blit(lose2, (200, 200))
        
        
    clock.tick(FPS)        
    display.update()