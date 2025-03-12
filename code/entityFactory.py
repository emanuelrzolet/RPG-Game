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
                return Player('player', (0, altura / 2))