import pygame
from player import *
from pieces import *

pygame.init()
import pygame.freetype
pygame.freetype.init()
#setup
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")
board = pygame.transform.scale(pygame.image.load("images/Board.png"),(650, 650))
movecircle = pygame.transform.scale(pygame.image.load("images/circle.png"),(50, 25))
FPS = 60
WHITE = (255,255,255)
BLACK = (49,46,43)
GREY = (152,150,149)

def createpiece(name, colour, position): #helper function to efficiently create pieces 
    if(name == "Rook"):
        return Rook(colour, position)
    if(name == "Bishop"):
        return Bishop(colour, position)
    if(name == "Queen"):
        return Queen(colour, position)
    if(name == "King"):
        return King(colour, position)
    if(name == "Knight"):
        return Knight(colour, position)
    
def updateboard():
    WIN.fill(BLACK)
    WIN.blit(board, (50,50))
    for i in WhitePlayer.pieces:
        WIN.blit(i.sprite, i.position)
    for i in BlackPlayer.pieces:
        WIN.blit(i.sprite, i.position)
    pygame.display.update() 

def main():

    #setup
    global WhitePlayer
    global BlackPlayer
    WhitePlayer = Player("White")
    BlackPlayer = Player("Black")
    for i in range(0,8): #pond placement
        BlackPlayer.pieces.append(Pond("Black", (70.5+(77.5*i), 131.7)))
        WhitePlayer.pieces.append(Pond("White", (70.5+(77.5*i), 515.2)))
    names = ["Rook","Knight", "Bishop", "Queen","King","Bishop", "Knight", "Rook"]
    for i in range(0,8):#first ranks
        BlackPlayer.pieces.append(createpiece(names[i], "Black",(70.5+(77.5*i), 55.0)))
        WhitePlayer.pieces.append(createpiece(names[i], "White",(70.5+(77.5*i), 591.9)))
    
    #game functionality
    clock=pygame.time.Clock()
    while True:
        moveable = []
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked_pos = pygame.mouse.get_pos()
                for i in WhitePlayer.pieces:
                    if((clicked_pos[0] > i.position[0]) and (clicked_pos[0] < i.position[0]+77.5) and (clicked_pos[1] > i.position[1]) and (clicked_pos[1] < i.position[1]+76.7)):
                        piece = i
                        if(i.name=="King"):
                            moveable = i.movement(BlackPlayer,WhitePlayer, False)
                        else:
                            moveable = i.movement(BlackPlayer,WhitePlayer)
                        
                        print("hey")
                        break
                if (len(moveable) > 0):
                    move = True
                    while(move==True):
                        for l in moveable:
                            WIN.blit(movecircle, (l[0]+15.5, l[1]+27))
                            pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                            if (event.type == pygame.MOUSEBUTTONDOWN):
                                clicked_pos = pygame.mouse.get_pos()
                                for i in moveable:
                                    if((clicked_pos[0] > i[0]) and (clicked_pos[0] < i[0]+77.5) and (clicked_pos[1] > i[1]) and (clicked_pos[1] < i[1]+76.7)):
                                        new_pos=(round(i[0], 1), round(i[1], 1))
                                        for j in BlackPlayer.pieces:
                                            if j.position == new_pos:
                                                BlackPlayer.pieces.remove(j)
                                                break 
                                        piece.position = new_pos
                                        move = False
                                        break
                            
                                    
                    
        updateboard()

if __name__=="__main__":
  main()