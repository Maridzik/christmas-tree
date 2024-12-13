import pygame


def kirill_paint(screen, x, y, mode=None):
    toy = pygame.image.load("kirill_decoration.png").convert_alpha()
    screen.blit(toy, (x - toy.get_width() // 2, y - toy.get_height() // 2))
