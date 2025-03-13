import pygame
import random

from code.entity import Entity
from code.entityFactory import EntityFactory
from code.enemy import Enemy

class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.player = EntityFactory.get_entity('player')
        self.entity_list.append(self.player)
        self.enemy_group = pygame.sprite.Group()
        self.enemy_timer = 0
        self.enemy_interval = 60
        self.clock = pygame.time.Clock()  # Cria um objeto Clock
        try:
            self.background = pygame.image.load("./assets/background_1.png").convert_alpha()
        except pygame.error as e:
            print(f"Erro ao carregar a imagem de fundo: {e}")
            self.background = None

    def run(self):
        self.window.fill((0, 0, 0))
        if self.background:
            self.window.blit(self.background, (0, 0))
        self.window.blit(self.player.image, self.player.rect)
        self.player.projectile_group.draw(self.window)
        self.enemy_group.draw(self.window)
        pygame.display.flip()

    def game_loop(self):
        executando = True
        while executando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    executando = False
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if evento.button == 1:
                        self.player.shoot(pygame.mouse.get_pos())

            self.player.update()
            self.enemy_group.update()
            self.generate_enemies()
            self.check_collisions()  # Verifica colisões
            self.run()
            self.clock.tick(60)  # Limita a taxa de quadros a 60 FPS


        pygame.quit()

    def generate_enemies(self):
        self.enemy_timer += 1
        if self.enemy_timer >= self.enemy_interval:
            self.enemy_timer = 0
            side = random.choice(["top", "bottom", "left", "right"])
            if side == "top":
                x = random.randint(0, self.window.get_width())
                y = 0
            elif side == "bottom":
                x = random.randint(0, self.window.get_width())
                y = self.window.get_height()
            elif side == "left":
                x = 0
                y = random.randint(0, self.window.get_height())
            elif side == "right":
                x = self.window.get_width()
                y = random.randint(0, self.window.get_height())
            enemy_type = random.choice(["square", "circle"])
            enemy = Enemy((x, y), self.player, enemy_type)
            self.enemy_group.add(enemy)

    def check_collisions(self):
        # Colisão com projéteis
        collisions = pygame.sprite.groupcollide(self.player.projectile_group, self.enemy_group, True, True)
        # Colisão com o jogador
        player_collisions = pygame.sprite.spritecollide(self.player, self.enemy_group, True)