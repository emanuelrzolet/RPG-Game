import pygame

# Inicializa o Pygame
pygame.init()

# Obtém informações sobre o dispositivo de exibição
info = pygame.display.Info()

# Obtém a largura e altura da tela
largura = info.current_w / 2
altura = info.current_h / 2

# Cria uma janela com a resolução da tela
tela = pygame.display.set_mode((largura, altura))

# Loop principal do jogo
while True:
    # Processa eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Desenha na tela
    tela.fill((0, 0, 0))  # Preenche a tela com preto
    
    pygame.draw.circle(tela, "red",(200,200),4)
    
    pygame.display.flip()  # Atualiza a tela