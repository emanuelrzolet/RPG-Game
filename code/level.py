#!/usr/bin/python
# -*- coding: utf-8 -*-

class Level:
    def __init__(self,window):
        self.window = window

    def run(self):
        self.window.fill((0, 0, 0)) # Fundo preto
