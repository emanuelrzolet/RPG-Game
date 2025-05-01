from abc import ABC, abstractmethod
import pygame

class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.rect = pygame.Rect(position[0], position[1], 0, 0)  # Retângulo inicial
        self.speed = 0

    @abstractmethod
    def move(self):
        pass