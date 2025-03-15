import pygame
from code.player import Player

class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, positions=(0, 0)):
        info = pygame.display.Info()
        largura = info.current_w
        altura = info.current_h
        match entity_name:
            case 'player':
                return Player('player', (largura / 4, altura / 2)) # muda a posição inicial do player
            case 'enemy':
                pass