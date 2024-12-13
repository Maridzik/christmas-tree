import pygame
from random import randrange


def eva_paint(screen, pos):
    mylist = ['игрушка11.png', 'игрушка21.png']
    imp = pygame.image.load(mylist[randrange(0, 2)])
    screen.blit(pygame.transform.scale(imp, (30, 30)), (pos[0] - 15, pos[1]))