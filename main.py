import pygame
from player import *
from pieces import *
from game import *

pygame.init()
pygame.freetype.init()

def main():

    setup()
    clock=pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked_pos = pygame.mouse.get_pos()
                compute_action(clicked_pos)
    
        updateboard()

if __name__=="__main__":
  main()