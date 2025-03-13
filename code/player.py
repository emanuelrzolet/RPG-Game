import pygame
from code.const import ENTITY_SPEED
from code.entity import Entity
from code.projectile import Projectile
import math

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.projectile_group = pygame.sprite.Group()
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=position)
        self.draw_triangle()

    def draw_triangle(self):
        points = [(self.rect.width / 2, 0), (0, self.rect.height), (self.rect.width, self.rect.height)]
        pygame.draw.polygon(self.image, (255, 255, 255), points)

    def move(self):
        info = pygame.display.Info()
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_w] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_s] and self.rect.bottom < info.current_h:
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_a] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_d] and self.rect.right < info.current_w:
            self.rect.centerx += ENTITY_SPEED[self.name]
    def shoot(self, target):
        projectile = Projectile(self.rect.center, target)
        self.projectile_group.add(projectile)

    def update(self):
        self.move()  # Chama o método move
        self.projectile_group.update()