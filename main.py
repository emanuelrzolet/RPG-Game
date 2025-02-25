import pygame
# Inicialização do pygame e da janela
print("Sistem start")
pygame.init()
screen = pygame.display.set_mode(size=(600,480))
print("Sistem end")
print("Loop start")
while True:
    # Check for all Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #Close screen
            print("Saindo")
            quit() #end pygame