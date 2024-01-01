import pygame
import math
from pieces import *
from player import *
from screen import *
from computer import skill_bot2
import pygame.freetype

global WhitePlayer
global BlackPlayer
global checkmate

checkMate = False
WIDTH, HEIGHT = 750, 750
WHITE = (255,255,255)
BLACK = (49,46,43)
GREY = (152,150,149)
board = pygame.transform.scale(pygame.image.load("images/Board.png"),(650, 650))
movecircle = pygame.transform.scale(pygame.image.load("images/circle.png"),(50, 25))

pygame.display.set_caption("Chess")

pygame.freetype.init()
font = pygame.freetype.Font("font.ttf", 22)

def playGame(WIN, diff):
    WhitePlayersTurn = True
    setUpInfo = setup()
    WhitePlayer = setUpInfo[0]
    BlackPlayer = setUpInfo[1]
    board_Info = setUpInfo[2]
    updateboard(WhitePlayer, BlackPlayer, WIN)
    checkMate = False
    staleMate = False
    while (checkMate == False and staleMate == False):
        staleMate = checkForStalemate(WhitePlayer, BlackPlayer, WhitePlayersTurn, board_Info)
        checkMate = checkForCheckMate(WhitePlayer, BlackPlayer, WhitePlayersTurn, board_Info)
        if (checkMate == False and staleMate == False):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked_pos = pygame.mouse.get_pos()
                    result = choose_piece(WhitePlayer, BlackPlayer, WIN, clicked_pos, WhitePlayersTurn, diff, board_Info)
                    pygame.display.update()
                    if(result != None):
                        if(result[0]!= None):
                            if(len(result[0])>0):
                                clicked_pos = None
                                while(clicked_pos == None):
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            pygame.quit()
                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                            clicked_pos = pygame.mouse.get_pos()
                                            result = move_piece(WhitePlayer, BlackPlayer, WIN, clicked_pos, result[0], result[1], WhitePlayersTurn, board_Info)
                                            if(result == True): # move was made
                                                if(WhitePlayersTurn == True):
                                                    WhitePlayersTurn = False
                                                else:
                                                    WhitePlayersTurn = True
                                                    
                updateboard(WhitePlayer, BlackPlayer, WIN)
                

            if(diff == "Noob"):
                if (WhitePlayersTurn == False):
                    if (checkMate == False and staleMate == False):
                        staleMate = checkForStalemate(WhitePlayer, BlackPlayer, WhitePlayersTurn, board_Info)
                        checkMate = checkForCheckMate(WhitePlayer, BlackPlayer, WhitePlayersTurn, board_Info)
                        if(staleMate == False and checkMate == False):
                            skill_bot2(WhitePlayer, BlackPlayer, WIN, diff, board_Info)
                        WhitePlayersTurn = True
                        updateboard(WhitePlayer, BlackPlayer, WIN)
                    else:
                        endScreen(WIN, checkMate, WhitePlayersTurn, diff)
            
    endScreen(WIN, checkMate, WhitePlayersTurn, diff)

def setup():
    WhitePlayer = Player("White")
    BlackPlayer = Player("Black")
    BlackPlayer.pieces = []
    BlackPlayer.points = 0
    WhitePlayer.pieces = []
    WhitePlayer.points = 0
    boardInfo = {}
    for i in range(0,8): #Pawn placement
        blackPawn = Pawn("Black", (70.5+(77.5*i), 131.7))
        whitePawn = Pawn("White", (70.5+(77.5*i), 515.2))
        BlackPlayer.pieces.append(blackPawn)
        WhitePlayer.pieces.append(whitePawn)
        boardInfo[blackPawn.position] = blackPawn
        boardInfo[whitePawn.position] = whitePawn
    names = ["Rook","Knight", "Bishop", "Queen","King","Bishop", "Knight", "Rook"]
    for i in range(0,8): #first ranks
        blackPiece = createpiece(names[i], "Black",(70.5+(77.5*i), 55.0))
        whitePiece = createpiece(names[i], "White",(70.5+(77.5*i), 591.9))
        BlackPlayer.pieces.append(blackPiece)
        WhitePlayer.pieces.append(whitePiece)
        boardInfo[blackPiece.position] = blackPiece
        boardInfo[whitePiece.position] = whitePiece
        if names[i] == "King":
            BlackPlayer.king = blackPiece
            WhitePlayer.king = whitePiece
    #fill empty slots with None
    return (WhitePlayer, BlackPlayer, boardInfo)

def createpiece(name, colour, position):
    """
        Helper function, takes in piece name, outputs instance of that piece object.
    """
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
    if(name == "Pawn"):
        return Pawn(colour, position) 
    
def checkForCheck(WhitePlayer, BlackPlayer, king, player, otherPlayer, board_Info):
    """
        Loops through all piece movements to determine if king is in check.(if king is being targetted)
    """
    for i in otherPlayer.pieces:
        if (i.name != "King"):
            if king.position in i.movement(BlackPlayer, WhitePlayer, board_Info):
                return (i, True)
    return (i, False)

def checkForStalemate(WhitePlayer, BlackPlayer, WhitePlayersTurn, board_Info):
    if(WhitePlayersTurn == True):
        player = WhitePlayer
    else:
        player = BlackPlayer
    for i in player.pieces:
        if i.name == "King":
            if len(i.movement(BlackPlayer, WhitePlayer, board_Info, False)) > 0:
                   return False
        else:
            if len(i.movement(BlackPlayer, WhitePlayer, board_Info)) > 0:
                return False
    return True
                   

def checkForCheckMate(WhitePlayer, BlackPlayer, WhitePlayersTurn, board_Info):
    #find players turn
    if(WhitePlayersTurn == True):
        player = WhitePlayer
        otherPlayer = BlackPlayer
    else:
        player = BlackPlayer
        otherPlayer = WhitePlayer
    #find king
    king = player.king
    result = checkForCheck(WhitePlayer, BlackPlayer, king, player, otherPlayer, board_Info)

    checkingPiece = result[0]
    if checkingPiece.name == "King":
        checkmovement = checkingPiece.movement(BlackPlayer, WhitePlayer, board_Info, False)
    else:
        checkmovement = checkingPiece.movement(BlackPlayer, WhitePlayer, board_Info)
    if(result[1] == True):#if in check
        if(len(king.movement(BlackPlayer, WhitePlayer, board_Info, False)) == 0):
            for j in player.pieces:
                if(j.name != "King"):
                    movement = j.movement(BlackPlayer, WhitePlayer, board_Info)
                    if (len(movement)>0):
                        for i in movement:
                            if((i in checkmovement) and i != king.position):
                                if (((king.position[0] <= i[0] and i[0] <= checkingPiece.position[0]) and (king.position[1] <= i[1] and i[1] <= checkingPiece.position[1]))
                                or 
                                ((king.position[0] <= i[0] and i[0] <= checkingPiece.position[0]) and (king.position[1] >= i[1] and i[1] >= checkingPiece.position[1]))
                                or 
                                ((king.position[0] >= i[0] and i[0] >= checkingPiece.position[0]) and (king.position[1] >= i[1] and i[1] >= checkingPiece.position[1])) 
                                or 
                                ((king.position[0] >= i[0] and i[0] >= checkingPiece.position[0]) and (king.position[1] <= i[1] and i[1] <= checkingPiece.position[1]))):
                                    return False
            return True
    return False
    

def choose_piece(WhitePlayer, BlackPlayer, WIN, clicked_pos, WhitePlayersTurn, diff, board_info):
    """
        Outputs the available positions to move to for the piece selected by user if it can move.
    """
    moveable = []
    piece = None
    #find players turn
    if(WhitePlayersTurn == True):
        player = WhitePlayer
        otherPlayer = BlackPlayer
    else:
        player = BlackPlayer
        otherPlayer = WhitePlayer
    #find king
    king = player.king
    clickedSquare = find_square(clicked_pos)
    result = checkForCheck(WhitePlayer, BlackPlayer, king, player, otherPlayer, board_info) 
    checkingPiece = result[0]
    check = result[1]
    if(check == True): #if king is in check, force the king to move or force another piece to protect the king
            #move king
            if(clickedSquare == king.position):
                moveable = king.movement(BlackPlayer,WhitePlayer, board_info, False)
                piece = king
            #block your king from check
            elif(clickedSquare in board_info):
                if otherPlayer.colour != board_info[clickedSquare].colour:
                    potential_piece = board_info[clickedSquare]
                    #loop through the movements of all your pieces 
                    intercepts=[]
                    if potential_piece.name == "King":
                        movement = potential_piece.movement(BlackPlayer, WhitePlayer, board_info, False)
                    else:
                        movement = potential_piece.movement(BlackPlayer, WhitePlayer, board_info)
                    for j in movement:
                        #if one of your pieces movements intercept the checking pieces movement which is not your king (obviously)
                        if(j == checkingPiece.position):
                            intercepts.append(j)
                        checkmovement = checkingPiece.movement(BlackPlayer, WhitePlayer, board_info)
                        if((j in checkmovement) and j != king.position):
                            if (((king.position[0] <= j[0] and j[0] <= checkingPiece.position[0]) and (king.position[1] <= j[1] and j[1] <= checkingPiece.position[1]))
                            or 
                            ((king.position[0] <= j[0] and j[0] <= checkingPiece.position[0]) and (king.position[1] >= j[1] and j[1] >= checkingPiece.position[1]))
                            or 
                            ((king.position[0] >= j[0] and j[0] >= checkingPiece.position[0]) and (king.position[1] >= j[1] and j[1] >= checkingPiece.position[1])) 
                            or 
                            ((king.position[0] >= j[0] and j[0] >= checkingPiece.position[0]) and (king.position[1] <= j[1] and j[1] <= checkingPiece.position[1]))):
                                intercepts.append(j)
                                
                        if(len(intercepts)>0):
                            moveable = intercepts
                            piece = potential_piece

            if(piece == None):
                return ([], None)
    else:     
        if (not (clickedSquare in board_info)):
            return ([], None)
        else:
            piece = board_info[clickedSquare]
            if piece.colour != player.colour:
                return ([], None)
            position_holder = piece.position
            piece.position = (1000,1000) 
            result = checkForCheck(WhitePlayer, BlackPlayer, king, player, otherPlayer, board_info)
            if(result[1] == True): #king is pinned, move temp piece back to original position, return none
                piece.position = position_holder
                return [[], None, False]
            #king is not pinned, proceed.
            piece.position = position_holder 
            if(piece.name=="King"):
                moveable = piece.movement(BlackPlayer,WhitePlayer, board_info, False)
            else:
                moveable = piece.movement(BlackPlayer,WhitePlayer, board_info)
    #Show where your piece can move once it is successfully chosen.
    if diff != "No_Bot":
        if (WhitePlayersTurn == False):
            return (moveable, piece, False)
    for l in moveable:
        WIN.blit(movecircle, (l[0]+15.5, l[1]+27))
    return (moveable, piece, False)


def move_piece(WhitePlayer, BlackPlayer, WIN, clicked_pos, moveable, piece, WhitePlayersTurn, board_Info):
    """
        Moves selected piece to the position chosen by the user.
        This fuction is used along with the 'choose_piece' function once it shows available positions for chosen piece to move to.
    """
    moved = False
    
    #identify whos moving
    if(WhitePlayersTurn == True):
        player = WhitePlayer
        otherPlayer = BlackPlayer
    else:
        player = BlackPlayer
        otherPlayer = WhitePlayer

    #check if user clicked on a movable spot or not
    new_pos = find_square(clicked_pos)
    if(new_pos in moveable):
        if(new_pos in board_Info):
            enemyPiece = board_Info[new_pos]
            otherPlayer.pieces.remove(enemyPiece)
            player.points += enemyPiece.points

        #animation for the piece to slide rather than to blink positions
        shift=15
        board_Info.pop(piece.position)
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
            if WIN != None:
                updateboard(WhitePlayer, BlackPlayer, WIN)
        moved = True
        board_Info[new_pos] = piece


    #if player moved piece, return true to change the turn
    if (moved == True):
        return True
    else:
        return False

def updateboard(WhitePlayer, BlackPlayer, WIN):
    """
        reprints board and all pieces in their current position.
    """
    WIN.fill(BLACK)
    WIN.blit(board, (50,50))
    for i in WhitePlayer.pieces:
        WIN.blit(i.sprite, i.position)
    for i in BlackPlayer.pieces:
        WIN.blit(i.sprite, i.position)
    font.render_to(WIN, (300,25), ("Black Points: " + str(BlackPlayer.points)), (WHITE))
    font.render_to(WIN, (300,707), ("White Points: " + str(WhitePlayer.points)), (WHITE))
    pygame.display.update() 

def find_square(clickedpos):
    #x starts 70.5 ends 690.5
    #y starts 55.0 ends 669.4
    #sq size is x=77.5 and y=76.7
    i=0
    j=0
    currx = clickedpos[0] - 70.5
    curry = clickedpos[1] - 55.0
    while ((currx - 77.5*i) > 0):
        i+=1
    while ((curry - 76.7*j) > 0):
        j+=1
    return (70.5+((i-1)*77.5), 55+((j-1)*76.7))
    