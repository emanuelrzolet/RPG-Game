import json
import pygame

from code.menu import Menu
class Game:
    def __init__(self):
        # Inicializa o Pygame
        pygame.init()

        # Obtém informações sobre o dispositivo de exibição
        info = pygame.display.Info()

        # Obtém a largura e altura da tela
        largura = info.current_w / 2
        altura = info.current_h / 2

        # Cria uma janela com a resolução da tela
        self.window = pygame.display.set_mode((largura, altura))
        
        # Cria um arquivo Json com as constantes
        resolucao = (info.current_w, info.current_h)
        def salvar_constantes(dados, arquivo="constantes.json"):
            with open(arquivo, "w") as f:
                json.dump(dados, f)
        salvar_constantes(resolucao)
        
        
        
        
    def run(self):
        # Loop principal do jogo
        while True:
            # Processa eventos
            # Chamada do Menu e criação da classe
            menu = Menu(self.window)
            menu.run()