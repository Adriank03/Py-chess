import random
import threading 
import copy
from pieces import *

def noob_bot_turn(WIN, BlackPlayer, diff):
    from game import choose_piece, move_piece
    result = ([], None)
    
    while (True):
        num = random.randint(0, len(BlackPlayer.pieces)-1)
        clicked_pos = BlackPlayer.pieces[num].position
        result = choose_piece(WIN, (clicked_pos[0]+1, clicked_pos[1]+1), False, diff)
        if(result != None):
            if len(result[0]) > 0:
                break
    if(result[0] != None):
        num2 = random.randint(0, len(result[0])-1)
        clicked_pos = result[0][num2]
        move_piece(WIN, (clicked_pos[0]+1, clicked_pos[1]+1), result[0], result[1], False)
    
def skill_bot2(WhitePlayer, BlackPlayer, WIN, diff, board_Info):
    from game import choose_piece, move_piece
    blackmax = -1000
    threads = []
    output=[]
    for i in BlackPlayer.pieces:
        result = choose_piece(WhitePlayer, BlackPlayer, WIN, (i.position[0]+1, i.position[1]+1), False, diff, board_Info)
        if(result != None):
            if (len(result[0])>0):
                for j in result[0]:
                    threads.append(threading.Thread(target=handle, args=(WhitePlayer, BlackPlayer, WIN, diff, board_Info, i, j, output, 1)))
    for thread in threads:
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()
    for l in output:
        if l[0]>blackmax:
            blackmax = l[0]
            bestmoveinfo = l[1]
            
    move_piece(WhitePlayer, BlackPlayer, WIN, bestmoveinfo[0], bestmoveinfo[1], bestmoveinfo[2], False, board_Info)

def handle(WhitePlayer, BlackPlayer, WIN, diff, board_Info, i, j, results, depth):
    move = work(WhitePlayer, BlackPlayer, WIN, diff, board_Info, i, j, depth)
    results.append(move)
    

def work(WhitePlayer, BlackPlayer, WIN, diff, board_Info, i, j, depth):
    from game import choose_piece, move_piece
    copies = create_copy(WhitePlayer, BlackPlayer, board_Info)
    WhiteCopy = copies[0]
    BlackCopy = copies[1]
    board_copy = copies[2]
    result2 = choose_piece(WhiteCopy, BlackCopy, WIN, (i.position[0]+1, i.position[1]+1), False, diff, board_copy)
    move_piece(WhiteCopy, BlackCopy, None, (j[0]+1, j[1]+1), result2[0], result2[1], False, board_copy)
    stats = minimax(WIN, WhiteCopy, BlackCopy, True, depth, diff, board_copy)
    return (stats, ((j[0]+1, j[1]+1), result2[0], i))

def minimax(WIN, WhitePlayer, BlackPlayer, WhitePlayersTurn, depth, diff, board_Info):
    from game import choose_piece
    if depth == 0:
        print("reached depth 0")
        return BlackPlayer.points - WhitePlayer.points
    else:
        output2 = []
        threads=[]
        if WhitePlayersTurn == False: #black player turn, use max
            for i in BlackPlayer.pieces:
                result = choose_piece(WhitePlayer, BlackPlayer, WIN, (i.position[0]+1, i.position[1]+1), False, diff, board_Info)
                if(result != None):
                    if (len(result[0])>0):
                        for j in result[0]:
                            threads.append(threading.Thread(target=handle2, args=(WhitePlayer, BlackPlayer, WIN, diff, board_Info, i, j, output2, (depth-1), WhitePlayersTurn,)))
            for thread in threads:
                thread.start()
            # Wait for all threads to finish
            for thread in threads:
                thread.join()
            return max(output2)
            
                        
        else: #White player turn, use min
            for i in WhitePlayer.pieces:
                result = choose_piece(WhitePlayer, BlackPlayer, WIN, (i.position[0]+1, i.position[1]+1), True, diff, board_Info)
                if(result != None):
                    if (len(result[0])>0):
                        for j in result[0]:
                            threads.append(threading.Thread(target=handle2, args=(WhitePlayer, BlackPlayer, WIN, diff, board_Info, i, j, output2, (depth-1), WhitePlayersTurn,)))
            for thread in threads:
                thread.start()
            # Wait for all threads to finish
            for thread in threads:
                thread.join()
            print(output2)
            return min(output2)

def handle2(WhitePlayer, BlackPlayer, WIN, diff, board_Info, i, j, output, depth, WhitePlayersTurn):
    move = work2(WhitePlayer, BlackPlayer, WIN, diff, board_Info, i, j, depth, WhitePlayersTurn)
    output.append(move)

def work2(WhitePlayer, BlackPlayer, WIN, diff, board_Info, i, j, depth, WhitePlayersTurn):
    from game import choose_piece, move_piece
    if WhitePlayersTurn == True:
        next=False
    else:
        next=True
    copies = create_copy(WhitePlayer, BlackPlayer, board_Info)
    WhiteCopy = copies[0]
    BlackCopy = copies[1]
    board_copy = copies[2]
    result2 = choose_piece(WhiteCopy, BlackCopy, WIN, (i.position[0]+1, i.position[1]+1), WhitePlayersTurn, diff, board_copy)
    move_piece(WhiteCopy, BlackCopy, None, (j[0]+1, j[1]+1), result2[0], result2[1], WhitePlayersTurn, board_copy)
    return minimax(WIN, WhiteCopy, BlackCopy, next, depth, diff, board_copy)

def create_copy(WhitePlayer, BlackPlayer, board_Info):
    from player import Player
    from game import createpiece
    Whitecopy = Player(WhitePlayer.colour)
    Blackcopy = Player(BlackPlayer.colour)
    new_board = {}

    Whitecopy.points = WhitePlayer.points
    for i in WhitePlayer.pieces:
        piece = createpiece(i.name, i.colour, i.position)
        Whitecopy.pieces.append(piece)
        if i.name == "King":
            Whitecopy.king = piece
        new_board[i.position] = piece

    Blackcopy.points = BlackPlayer.points
    for i in BlackPlayer.pieces:
        piece = createpiece(i.name, i.colour, i.position)
        Blackcopy.pieces.append(piece)
        if i.name == "King":
            Blackcopy.king = piece
        new_board[i.position] = piece
    

    return (Whitecopy, Blackcopy, new_board)
 