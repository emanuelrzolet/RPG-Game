import pygame

from code.menu import Menu, Level

class Game:
    def __init__(self):
        pygame.init()
        info = pygame.display.Info()
        largura = info.current_w / 2
        altura = info.current_h / 2
        self.window = pygame.display.set_mode((largura, altura))
        self.game_state = "menu"  # Estado inicial do jogo

    def run(self):
        while True:
            if self.game_state == "menu":
                menu = Menu(self.window)
                if menu.run():
                    self.game_state = "level"  # Muda para o estado do nível
            elif self.game_state == "level":
                level = Level(self.window, name="Level1")
                level.game_loop() # inicia o loop do level
                self.game_state = "menu" # retorna ao menu após o loop do level terminar