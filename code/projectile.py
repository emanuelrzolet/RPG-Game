import pygame
import math

class Projectile(pygame.sprite.Sprite):
    def __init__(self, position, target, speed=2):
        super().__init__()
        self.image = pygame.Surface((10, 10), pygame.SRCALPHA)  # Superfície para desenhar o triângulo
        self.rect = self.image.get_rect(center=position)
        self.speed = speed
        self.target = target
        self.direction = self.calculate_direction()
        self.angle = 0
        self.draw_triangle()

    def draw_triangle(self):
        points = [(self.rect.width / 2, 0), (0, self.rect.height), (self.rect.width, self.rect.height)]
        pygame.draw.polygon(self.image, (255, 255, 255), points)  # Desenha o triângulo branco

    def calculate_direction(self):
        dx = self.target[0] - self.rect.centerx
        dy = self.target[1] - self.rect.centery
        distance = math.sqrt(dx**2 + dy**2)
        if distance == 0:
            return (0, 0)
        return (dx / distance, dy / distance)

    def update(self):
        self.rect.x += self.direction[0] * self.speed
        self.rect.y += self.direction[1] * self.speed
        self.angle += 10
        self.rotated_image = pygame.transform.rotate(self.image, self.angle)
        self.rotated_rect = self.rotated_image.get_rect(center=self.rect.center)

        # Remove o projétil se sair da tela
        screen_rect = pygame.display.get_surface().get_rect()
        if not screen_rect.colliderect(self.rect):
            self.kill()