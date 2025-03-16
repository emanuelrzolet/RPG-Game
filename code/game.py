import pygame

from code.menu import Menu, Level

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init() # Inicializa o mixer de áudio
        info = pygame.display.Info()
        largura = info.current_w / 2
        altura = info.current_h / 2
        self.window = pygame.display.set_mode((largura, altura))
        self.game_state = "menu"
        self.musica_tocando = False # Adiciona a variável de controle da música

    def tocar_musica(self):
        pygame.mixer.music.load("./assets/music.mp3") # Carrega a música
        pygame.mixer.music.play(-1) # Toca a música em loop

    def run(self):
        while True:
            if self.game_state == "menu":
                if not self.musica_tocando: # Verifica se a música já está tocando
                    self.tocar_musica() # Toca a música
                    self.musica_tocando = True
                menu = Menu(self.window)
                if menu.run():
                    self.game_state = "level"
            elif self.game_state == "level":
                level = Level(self.window, name="Level1")
                level.game_loop()
                self.game_state = "menu"