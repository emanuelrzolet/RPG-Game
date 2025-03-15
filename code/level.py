import pygame
import random

from code.entity import Entity
from code.entityFactory import EntityFactory
from code.enemy import Enemy, Heart

class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.player = EntityFactory.get_entity('player')
        self.entity_list.append(self.player)
        self.enemy_group = pygame.sprite.Group()
        self.heart_group = pygame.sprite.Group()
        self.enemy_timer = 0
        self.enemy_interval = 60
        self.clock = pygame.time.Clock()
        self.game_over = False
        self.font = pygame.font.Font(None, 36)
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
        self.heart_group.draw(self.window)
        self.draw_lives()
        pygame.display.flip()

    def draw_lives(self):
        for i in range(self.player.lives):
            pygame.draw.circle(self.window, (255, 0, 0), (20 + i * 30, 20), 10)

    def game_loop(self):
        executando = True
        while executando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    executando = False
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if evento.button == 1:
                        self.player.shoot(pygame.mouse.get_pos())

            if not self.game_over:
                self.player.update()
                self.enemy_group.update()
                self.generate_enemies()
                self.check_collisions()
                self.run()
            else:
                self.show_game_over()
            self.clock.tick(60)

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
        collisions = pygame.sprite.groupcollide(self.player.projectile_group, self.enemy_group, True, True)
        for enemies in collisions.values():
            for dead_enemy in enemies:
                heart = dead_enemy.drop_heart()
                if heart:
                    self.heart_group.add(heart)
        player_collisions = pygame.sprite.spritecollide(self.player, self.enemy_group, True)
        if player_collisions:
            self.player.take_damage()
            if self.player.lives <= 0:
                self.game_over = True
        heart_collisions = pygame.sprite.spritecollide(self.player, self.heart_group, True)
        if heart_collisions:
            self.player.heal()

    def show_game_over(self):
        game_over_text = self.font.render("Game Over", True, (255, 0, 0))
        game_over_rect = game_over_text.get_rect(center=(self.window.get_width() // 2, self.window.get_height() // 2 - 50))
        self.window.blit(game_over_text, game_over_rect)

        restart_text = self.font.render("Restart", True, (255, 255, 255))
        restart_rect = restart_text.get_rect(center=(self.window.get_width() // 2, self.window.get_height() // 2))
        self.window.blit(restart_text, restart_rect)

        menu_text = self.font.render("Menu", True, (255, 255, 255))
        menu_rect = menu_text.get_rect(center=(self.window.get_width() // 2, self.window.get_height() // 2 + 50))
        self.window.blit(menu_text, menu_rect)

        quit_text = self.font.render("Quit", True, (255, 255, 255))
        quit_rect = quit_text.get_rect(center=(self.window.get_width() // 2, self.window.get_height() // 2 + 100))
        self.window.blit(quit_text, quit_rect)

        pygame.display.flip()

        waiting_for_input = True # Adicionado para garantir que o loop continue até que uma opção seja escolhida

        while waiting_for_input: # Loop para verificar eventos continuamente
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_rect.collidepoint(event.pos):
                        self.__init__(self.window, self.name)
                        self.game_loop()
                        waiting_for_input = False # Sai do loop após escolher uma opção
                    elif menu_rect.collidepoint(event.pos):
                        self.game_over = False
                        waiting_for_input = False # Sai do loop após escolher uma opção
                        return
                    elif quit_rect.collidepoint(event.pos):
                        pygame.quit()
                        quit()