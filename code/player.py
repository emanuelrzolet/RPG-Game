import pygame
from code.entity import Entity
from code.projectile import Projectile
import math

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.projectile_group = pygame.sprite.Group()
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)  # Superfície para desenhar o triângulo
        self.rect = self.image.get_rect(center=position)
        self.draw_triangle()

    def draw_triangle(self):
        points = [(self.rect.width / 2, 0), (0, self.rect.height), (self.rect.width, self.rect.height)]
        pygame.draw.polygon(self.image, (255, 255, 255), points)  # Desenha o triângulo branco

    def move(self):
        # pressed_key = 
        pass

    def shoot(self, target):
        projectile = Projectile(self.rect.center, target)
        self.projectile_group.add(projectile)

    def update(self):
        self.projectile_group.update()