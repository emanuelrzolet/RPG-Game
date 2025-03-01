from code import menu
import pygame

from code.menu import Menu
#!/usr/bin/python
# -*- coding: utf-8 -*-

class Game:
    def __init__(self):
        pygame.init()
        # Inicialização do pygame e da janela
        self.window = pygame.display.set_mode(size=(600,480))

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu.run()
            # # Check for all Events
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         pygame.quit() #Close screen
            #         print("Saindo")
            #         quit() #end pygame