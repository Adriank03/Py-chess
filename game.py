import pygame
from pieces import *
from player import *
import math
import pygame.freetype

global WhitePlayer
global BlackPlayer
global WhitePlayersTurn
global check

WhitePlayer = Player("White")
BlackPlayer = Player("Black")
WhitePlayersTurn = True
WIDTH, HEIGHT = 750, 750
WHITE = (255,255,255)
BLACK = (49,46,43)
GREY = (152,150,149)
board = pygame.transform.scale(pygame.image.load("images/Board.png"),(650, 650))
movecircle = pygame.transform.scale(pygame.image.load("images/circle.png"),(50, 25))
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

pygame.freetype.init()
font = pygame.freetype.Font("font.ttf", 22)

def setup():
    for i in range(0,8): #pond placement
        BlackPlayer.pieces.append(Pond("Black", (70.5+(77.5*i), 131.7)))
        WhitePlayer.pieces.append(Pond("White", (70.5+(77.5*i), 515.2)))
    names = ["Rook","Knight", "Bishop", "Queen","King","Bishop", "Knight", "Rook"]
    for i in range(0,8):#first ranks
        BlackPlayer.pieces.append(createpiece(names[i], "Black",(70.5+(77.5*i), 55.0)))
        WhitePlayer.pieces.append(createpiece(names[i], "White",(70.5+(77.5*i), 591.9)))

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
    
def checkForCheck(king, player, otherPlayer):
    global check
    for i in player.pieces:
        if(i.name == "King"):
            king = i
            break
    for i in otherPlayer.pieces:
        if (i.name == "King"):
            for j in i.movement(BlackPlayer, WhitePlayer, False):
                if (j == king.position):
                    check = True
                    return i
        else:
            for j in i.movement(BlackPlayer, WhitePlayer):
                if (j == king.position):
                    check = True
                    return i
    check = False

def compute_action(clicked_pos):
    global WhitePlayersTurn
    global check
    moveable = []
    moved = False
    piece = None

    if(WhitePlayersTurn == True):
        player = WhitePlayer
        otherPlayer = BlackPlayer
    else:
        player = BlackPlayer
        otherPlayer = WhitePlayer

    for i in player.pieces:
        if(i.name == "King"):
            king = i
            break

    checkingPiece = checkForCheck(king, player, otherPlayer)
            
    if(check == True): #if king is in check, force the king to move or force another piece to protect the king
            if((clicked_pos[0] > king.position[0]) and (clicked_pos[0] < king.position[0]+77.5) and (clicked_pos[1] > king.position[1]) and (clicked_pos[1] < king.position[1]+76.7)):
                moveable = king.movement(BlackPlayer,WhitePlayer, False)
                piece = king
            else:
                for i in player.pieces:
                    temp=[]
                    if(i.name != "King"):
                        for j in i.movement(BlackPlayer, WhitePlayer):
                            if(((j in checkingPiece.movement(BlackPlayer, WhitePlayer)) and j != king.position) or j==checkingPiece.position):
                                temp_pond=Pond("White", j)
                                otherPlayer.pieces.append(temp_pond)
                                checkForCheck(king, player, otherPlayer)
                                if(check==False or j == checkingPiece.position):
                                    temp.append(j)
                                otherPlayer.pieces.remove(temp_pond)

                        if(len(temp)>0):
                            if((clicked_pos[0] > i.position[0]) and (clicked_pos[0] < i.position[0]+77.5) and (clicked_pos[1] > i.position[1]) and (clicked_pos[1] < i.position[1]+76.7)):
                                moveable = temp
                                piece = i
                                break
            if(piece == None):
                return


    else:                
        for i in player.pieces:
            if((clicked_pos[0] > i.position[0]) and (clicked_pos[0] < i.position[0]+77.5) and (clicked_pos[1] > i.position[1]) and (clicked_pos[1] < i.position[1]+76.7)):
                postion_holder = i.position
                i.position = (1000,1000)
                checkForCheck(king, player, otherPlayer)
                if(check == True):
                    i.position = postion_holder
                    return
                i.position = postion_holder
                piece = i
                if(i.name=="King"):
                    moveable = i.movement(BlackPlayer,WhitePlayer, False)
                else:
                    moveable = i.movement(BlackPlayer,WhitePlayer)
                break
    if(len(moveable) == 0):
        return 0
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
                            for j in otherPlayer.pieces:
                                if j.position == new_pos:
                                    player.points += j.points
                                    otherPlayer.pieces.remove(j)
                                    break
                            shift=15
                            while (piece.position != new_pos): 
                                if(piece.position[0] < new_pos[0]):
                                    diff = new_pos[0] - piece.position[0]
                                    if(diff < shift):
                                        piece.position = (piece.position[0]+(diff), piece.position[1])
                                    else:    
                                        piece.position = (piece.position[0]+shift, piece.position[1])
                                else:
                                    diff = piece.position[0]-new_pos[0]
                                    if(diff < shift):
                                        piece.position = (piece.position[0]-(diff), piece.position[1])
                                    else:    
                                        piece.position = (piece.position[0]-shift, piece.position[1])

                                if(piece.position[1] < new_pos[1]):
                                    diff = new_pos[1] - piece.position[1] 
                                    if(diff < shift):
                                        piece.position = (piece.position[0], piece.position[1]+(diff))
                                    else:    
                                        piece.position = (piece.position[0], piece.position[1]+shift)
                                else:
                                    diff = piece.position[1] - new_pos[1]
                                    if(diff < shift):
                                        piece.position = (piece.position[0], piece.position[1]-(diff))
                                    else:    
                                        piece.position = (piece.position[0], piece.position[1]-shift)
                                updateboard()
                                
                            moved = True
                            break
                    move = False
    if (moved == True):             
        if(WhitePlayersTurn == True):
            WhitePlayersTurn = False
        else:
            WhitePlayersTurn = True

def updateboard():
    WIN.fill(BLACK)
    WIN.blit(board, (50,50))
    for i in WhitePlayer.pieces:
        WIN.blit(i.sprite, i.position)
    for i in BlackPlayer.pieces:
        WIN.blit(i.sprite, i.position)
    font.render_to(WIN, (65,25), ("Black Points: " + str(BlackPlayer.points)), (WHITE))
    font.render_to(WIN, (65,707), ("White Points: " + str(WhitePlayer.points)), (WHITE))
    pygame.display.update() 