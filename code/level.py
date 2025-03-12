import pygame

from code.entity import Entity
from code.entityFactory import EntityFactory

class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.player = EntityFactory.get_entity('player')
        self.entity_list.append(self.player)
        try:
            self.background = pygame.image.load("./assets/background_1.png").convert_alpha()
        except pygame.error as e:
            print(f"Erro ao carregar a imagem de fundo: {e}")
            self.background = None

    def run(self):
        self.window.fill((0, 0, 0))
        if self.background:
            self.window.blit(self.background, (0, 0))
        self.window.blit(self.player.image, self.player.rect)  # Desenha a imagem do jogador
        self.player.projectile_group.draw(self.window)
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
            self.run()

        pygame.quit()