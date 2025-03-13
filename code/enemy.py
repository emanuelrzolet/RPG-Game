import pygame
import math
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, position, player, enemy_type):
        super().__init__()
        self.enemy_type = enemy_type
        if enemy_type == "square":
            self.image = pygame.Surface((20, 20))
            self.image.fill((0, 0, 255))  # Quadrado azul
        elif enemy_type == "circle":
            self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
            pygame.draw.circle(self.image, (255, 0, 0), (10, 10), 10)  # Círculo vermelho
        self.rect = self.image.get_rect(center=position)
        self.player = player
        self.speed = 1

    def update(self):
        direction = self.calculate_direction()
        self.rect.x += direction[0] * self.speed
        self.rect.y += direction[1] * self.speed

    def calculate_direction(self):
        dx = self.player.rect.centerx - self.rect.centerx
        dy = self.player.rect.centery - self.rect.centery
        distance = math.sqrt(dx**2 + dy**2)
        if distance == 0:
            return (0, 0)
        return (dx / distance, dy / distance)