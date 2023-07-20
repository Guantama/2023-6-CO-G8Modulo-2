import random

import pygame
from game.components.explosion import Explosion
from game.components.power_ups.hearth import Heart
from game.components.power_ups.bomb import Bomb
from game.components.power_ups.shield import Shield

from game.utils.constants import  SCREEN_WIDTH, SHIELD_TYPE, SPACESHIP_SHIELD


class PowerUpManager:
    MIN_TIME_POWER_UP = 5000
    MAX_TIME_POWER_UP = 10000

    def __init__(self):
        self.power_ups = []
        self.duration = random.randint(3, 5)
        self.when_appears = random.randint(5000, 10000)

    def update(self, game):
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)

            if game.player.rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                game.player.power_up_type = power_up.type
                game.player.has_power_up = True
                game.player.power_time_up = power_up.start_time + (self.duration * 2300)
                if game.player.power_up_type == SHIELD_TYPE:
                    game.player.set_image((65, 75), SPACESHIP_SHIELD)
                    self.power_ups = []
                elif game.player.power_up_type == "Heart":
                    game.player.lives += 1
                    self.power_ups = []
                elif game.player.power_up_type == "Bomb":
                    for enemy in game.enemy_manager.enemies:
                        explode = Explosion(enemy.rect.center)
                        game.all_sprites.add(explode)
                    game.enemy_manager.enemies = []
                    self.power_ups = []
                

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def generate_power_up(self):
        power_up_types = [Shield(), Heart(), Bomb()]
        while len(self.power_ups) < 3:  # Limitamos a 3 power-ups en pantalla
            power_up = random.choice(power_up_types)
            power_up.rect.x = random.randint(120, SCREEN_WIDTH - 120)
            power_up.rect.y = 0
            collides = pygame.sprite.spritecollide(power_up, self.power_ups, False)
            if not collides:
                self.power_ups.append(power_up)

    def reset(self):
        power_up = []
        now = pygame.time.get_ticks()
        self.when_appears = random.randint(now + self.MIN_TIME_POWER_UP, self.MAX_TIME_POWER_UP)