import pygame
import os
import random

TELA_LARGURA = 580
TELA_ALTURA = 808

IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png' )))
IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png' )))
IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png' )))
IMAGEM_PASSARO = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png' ))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png' ))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png' ))),
]

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50)


class Passaro:
    pass


class Cano:
    pass


class chao:
    pass