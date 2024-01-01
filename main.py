import pygame
from screen import *
pygame.init()

def main():

    WIN = pygame.display.set_mode((750, 750))
    clock=pygame.time.Clock()
    clock.tick(60)
    mainMenu(WIN)


if __name__=="__main__":
  main()  