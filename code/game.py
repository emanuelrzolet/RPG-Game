import pygame

from code.menu import Menu, Level
class Game:
    def __init__(self):
        # Inicializa o Pygame
        pygame.init()

        # Obtém informações sobre o dispositivo de exibição e a
        info = pygame.display.Info()

        # Obtém a largura e altura da tela
        largura = info.current_w / 2
        altura = info.current_h / 2

        # Cria uma janela com a resolução da tela
        self.window = pygame.display.set_mode((largura, altura))
        
        
    def run(self):
        # Loop principal do jogo
        while True:
            # Processa eventos
            # Chamada do Menu e criação da classe
            menu = Menu(self.window)
            # Se o retorno for true quer dizer que o laço vai finalizar pois foi clickado no botão de iniciar game
            menuReturn = menu.run()
            if menuReturn == True:
                level = Level(self.window, name="Level1")
                level.run()