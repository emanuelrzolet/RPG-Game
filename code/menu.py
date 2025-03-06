#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.level import Level

class Menu:
    def __init__(self, window):
        self.window = window
        self.atualizar_resolucao()
        self.font = pygame.font.Font(None, 36)

    def atualizar_resolucao(self):
        self.largura, self.altura = pygame.display.get_surface().get_size()
        self.botao_novo_jogo = Rect(self.largura // 2 - 100, self.altura // 2 - 100, 200, 50)
        self.botao_opcoes = Rect(self.largura // 2 - 100, self.altura // 2 - 25, 200, 50)
        self.botao_sair = Rect(self.largura // 2 - 100, self.altura // 2 + 50, 200, 50)

    def desenhar_texto(self, texto, pos, cor=(255, 255, 255)):
        texto_renderizado = self.font.render(texto, True, cor)
        texto_rect = texto_renderizado.get_rect(center=pos)
        self.window.blit(texto_renderizado, texto_rect)

    def desenhar_botoes(self):
        pygame.draw.rect(self.window, (0, 128, 255), self.botao_novo_jogo)
        pygame.draw.rect(self.window, (0, 128, 255), self.botao_opcoes)
        pygame.draw.rect(self.window, (0, 128, 255), self.botao_sair)
        self.desenhar_texto("Novo Jogo", self.botao_novo_jogo.center)
        self.desenhar_texto("Opções", self.botao_opcoes.center)
        self.desenhar_texto("Sair", self.botao_sair.center)

    def menu_opcoes(self):
        musica_ligada = True
        tela_cheia = False

        while True:
            botao_musica = Rect(self.largura // 2 - 100, self.altura // 2 - 150, 200, 50)
            botao_tela = Rect(self.largura // 2 - 100, self.altura // 2 - 75, 200, 50)
            botao_voltar = Rect(self.largura // 2 - 100, self.altura // 2, 200, 50)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if botao_musica.collidepoint(evento.pos):
                        musica_ligada = not musica_ligada
                    elif botao_tela.collidepoint(evento.pos):
                        tela_cheia = not tela_cheia
                        if tela_cheia:
                            pygame.display.set_mode((self.largura, self.altura), pygame.FULLSCREEN)
                        else:
                            pygame.display.set_mode((self.largura, self.altura))
                        self.atualizar_resolucao()
                    elif botao_voltar.collidepoint(evento.pos):
                        return

            self.window.fill((0, 0, 0))
            pygame.draw.rect(self.window, (0, 128, 255), botao_musica)
            pygame.draw.rect(self.window, (0, 128, 255), botao_tela)
            pygame.draw.rect(self.window, (0, 128, 255), botao_voltar)
            self.desenhar_texto(f"Música: {'Ligada' if musica_ligada else 'Desligada'}", botao_musica.center)
            self.desenhar_texto(f"Tela: {'Cheia' if tela_cheia else 'Janela'}", botao_tela.center)
            self.desenhar_texto("Voltar", botao_voltar.center)
            pygame.display.flip()

    def run(self):
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if self.botao_novo_jogo.collidepoint(evento.pos):
                        level = Level(self.window)
                        level.run()
                    elif self.botao_opcoes.collidepoint(evento.pos):
                        self.menu_opcoes()
                    elif self.botao_sair.collidepoint(evento.pos):
                        pygame.quit()
                        quit()

            self.window.fill((0, 0, 0))
            self.desenhar_botoes()
            pygame.display.flip()