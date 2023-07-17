from pygame.sprite import Sprite
import pygame
from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP

class Spaceship(Sprite):
    SHIP_WIDTH = 40
    SHIP_HEIGHT = 60
    X_POS = (SCREEN_WIDTH//2)- SHIP_WIDTH
    Y_POS = 500
    SHIP_SPEED = 10
    
    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image,(40, 60))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update (self, user_input):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        if user_input[pygame.K_RIGHT]:
            self.move_right()
        if user_input[pygame.K_UP]:
            self.move_up()
        if user_input[pygame.K_DOWN]:
            self.move_down()
   
    def move_left(self):
        self.rect.x -= self.SHIP_SPEED
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH

    def move_right(self):
        self.rect.x += self.SHIP_SPEED
        if self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0

    def move_right(self):
        self.rect.x += self.SHIP_SPEED
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def move_up(self):
        self.rect.y -= self.SHIP_SPEED
        if self.rect.top < 0:
            self.rect.top = 0

    def move_down(self):
        self.rect.y += self.SHIP_SPEED
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT