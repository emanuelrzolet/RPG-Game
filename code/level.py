import pygame

from code.entity import Entity

class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        try:
            self.background = pygame.image.load("./assets/background_1.png").convert_alpha() # Otimização
        except pygame.error as e:
            print(f"Erro ao carregar a imagem de fundo: {e}")
            self.background = None

    def run(self):
        self.window.fill((0, 0, 0))  # Fundo preto
        if self.background:
            self.window.blit(self.background, (0, 0))  # Desenha o background na posição (0,0)
        print("run foi chamada")
        pygame.display.flip()

    def game_loop(self):
        executando = True
        while executando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    executando = False

            self.run() # redesenha o level.

        pygame.quit()