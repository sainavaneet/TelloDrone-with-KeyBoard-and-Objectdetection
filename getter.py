import pygame
import sys


def init():
    pygame.init()
    window = pygame.display.set_mode((400, 400))


def getKey(keyName):
    ans = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    keyInput = pygame.key.get_pressed()
    keyNumber = getattr(pygame, 'K_{}'.format(keyName))

    if keyInput[keyNumber]:
        ans = True
    pygame.display.update()

    return ans





