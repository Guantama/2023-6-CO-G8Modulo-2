import pygame
from game.components.power_ups.power_up import PowerUp
from game.utils.constants import BOMB
class Bomb(PowerUp):
    def __init__(self):
        self.size = (40, 40)
        self.image = pygame.transform.scale(BOMB, self.size)
        super().__init__(self.image, type="Bomb")