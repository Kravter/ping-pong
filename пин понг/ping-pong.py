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
FPS = 60
clock = time.Clock()
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill((4, 245, 126))
        player2.update_l()
        balls.update()
        balls.reset()
        player1.update_r()
        player1.reset()
        player2.reset()
        
       
        
        
    clock.tick(FPS)        
    display.update()