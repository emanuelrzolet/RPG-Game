import pygame
class Game:
    def __init__(self):
        # Inicializa o Pygame
        pygame.__init__()

        # Obtém informações sobre o dispositivo de exibição
        info = pygame.display.Info()

        # Obtém a largura e altura da tela
        largura = info.current_w / 2
        altura = info.current_h / 2

        # Cria uma janela com a resolução da tela
        tela = pygame.display.set_mode((largura, altura))
        
        
        def run():
            # Loop principal do jogo
            while True:
                # Processa eventos
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        pygame.quit()
                        quit()

            