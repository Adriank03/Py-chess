import pygame

hshift, vshift = 77.5, 76.7
PieceWidth, PieceHeight = 80, 80

class Piece():
    def __init__(self, colour, position):
        self.colour = colour
        self.position = position
        

    def movement(self, BlackPlayer, WhitePlayer, board_Info):
        """
            Abstract method, should return pieces unique movement.
        """
        return []

class Pawn(Piece):
    def __init__(self, colour, position):
        super().__init__(colour, position)
        self.name = "Pawn"
        self.sprite = pygame.transform.smoothscale(pygame.image.load("images/" + colour + "_Pawn.png"),(PieceWidth, PieceHeight))
        self.points = 1
    
    def movement(self, BlackPlayer, WhitePlayer, board_Info):
        moves = []
        blocked = False
        #for the white Pawn
        if (self.colour == "White"):
            shiftedy=round(self.position[1]-76.7, 1)
            pos=(self.position[0]-77.5, shiftedy)
            if(pos in board_Info):
                piece = board_Info[pos]
                if piece.colour == "Black":
                    moves.append(piece.position)
            pos=(self.position[0]+77.5, shiftedy)
            if(pos in board_Info):
                piece = board_Info[pos]
                if piece.colour == "Black":
                    moves.append(piece.position)
            pos=(self.position[0], shiftedy)
            if(not (pos in board_Info)):
                moves.append(pos)

        if (self.colour == "Black"):
            shiftedy=round(self.position[1]+76.7, 1)
            pos=(self.position[0]-77.5, shiftedy)
            if(pos in board_Info):
                piece = board_Info[pos]
                if piece.colour == "White":
                    moves.append(piece.position)
            pos=(self.position[0]+77.5, shiftedy)
            if(pos in board_Info):
                piece = board_Info[pos]
                if piece.colour == "White":
                    moves.append(piece.position)
            pos=(self.position[0], shiftedy)
            if(not (pos in board_Info)):
                moves.append(pos)
        return moves

class Rook(Piece):
    def __init__(self, colour, position):
        super().__init__(colour, position)
        self.name = "Rook"
        self.sprite = pygame.transform.smoothscale(pygame.image.load("images/" + colour + "_Rook.png"),(PieceWidth, PieceHeight))
        self.points = 5

    def movement(self, BlackPlayer, WhitePlayer, board_Info):
        moves = []
        #up
        i=1
        while(i<8):
            shiftedy = round(self.position[1]-(76.7*i), 1)
            pos = (self.position[0], shiftedy)
            if shiftedy < 55.0:
                break
            if (not (pos in board_Info)):
                moves.append(pos)
            else:
                piece = board_Info[pos]
                if(self.colour == "Black"):
                    if(piece.colour == "White"):
                        moves.append(pos)
                        break
                    else:
                        break
                if(self.colour == "White"):
                    if(piece.colour == "Black"):
                        moves.append(pos)
                        break
                    else:
                        break
            i+=1
        #down
        i=1
        while(i<8):
            shiftedy = round(self.position[1]+(76.7*i), 1)
            pos = (self.position[0], shiftedy)
            if shiftedy > 591.9:
                break
            if (not (pos in board_Info)):
                moves.append(pos)
            else:
                piece = board_Info[pos]
                if(self.colour == "Black"):
                    if(piece.colour == "White"):
                        moves.append(pos)
                        break
                    else:
                        break
                if(self.colour == "White"):
                    if(piece.colour == "Black"):
                        moves.append(pos)
                        break
                    else:
                        break
            i+=1

        #left
        i=1
        while(i<8):
            shiftedx = round(self.position[0]-(77.5*i), 1)
            pos = (shiftedx, self.position[1])
            if shiftedx < 70.5:
                break
            if (not (pos in board_Info)):
                moves.append(pos)
            else:
                piece = board_Info[pos]
                if(self.colour == "Black"):
                    if(piece.colour == "White"):
                        moves.append(pos)
                        break
                    else:
                        break
                if(self.colour == "White"):
                    if(piece.colour == "Black"):
                        moves.append(pos)
                        break
                    else:
                        break   
            i+=1            
        #right
        i=1
        while(i<8):
            shiftedx = round(self.position[0]+(77.5*i), 1)
            pos = (shiftedx, self.position[1])
            if shiftedx > 613:
                break
            if (not (pos in board_Info)):
                moves.append(pos)
            else:
                piece = board_Info[pos]
                if(self.colour == "Black"):
                    if(piece.colour == "White"):
                        moves.append(pos)
                        break
                    else:
                        break
                if(self.colour == "White"):
                    if(piece.colour == "Black"):
                        moves.append(pos)
                        break
                    else:
                        break
            i+=1                
        return moves
    
class Bishop(Piece):
    def __init__(self, colour, position):
        super().__init__(colour, position)
        self.name = "Bishop"
        self.sprite = pygame.transform.smoothscale(pygame.image.load("images/" + colour + "_Bishop.png"),(PieceWidth, PieceHeight))
        self.points = 3

    def movement(self, BlackPlayer, WhitePlayer, board_Info):
        moves = []
        #upleft

        positions = [(-77.5, -76.7), (77.5, -76.7), (-77.5, 76.7), (77.5, 76.7)]
        for j in range(0,4):
            i=1
            while(i<8):
                currpos = (round(self.position[0]+(i*positions[j][0]), 1), round(self.position[1]+(i*positions[j][1]), 1))
                if ((currpos[0]<70.5 or currpos[0]>613) or (currpos[1]<55 or currpos[1]>591.9)):
                    break
                if not(currpos in board_Info):
                    moves.append(currpos)
                else:
                    if self.colour == "Black":
                        if board_Info[currpos].colour == "White":
                            moves.append(currpos)
                            break
                        else:
                            break
                    if self.colour == "White":
                        if board_Info[currpos].colour == "Black":
                            moves.append(currpos)
                            break
                        else:
                            break
                i+=1
        return moves
    
class Knight(Piece):
    def __init__(self, colour, position):
        super().__init__(colour, position)
        self.name = "Knight"
        self.sprite = pygame.transform.smoothscale(pygame.image.load("images/" + colour + "_Knight.png"),(PieceWidth, PieceHeight))
        self.points = 3

    def movement(self, BlackPlayer, WhitePlayer, board_Info):
        #print("moving knight for " + self.colour)
        moves = []
        positions = [(-77.5,-76.7*2), (77.5, -76.7*2), (77.5*2, -76.7), (77.5*2, 76.7), (77.5, 76.7*2), (-77.5, 76.7*2), 
                     (-77.5*2, 76.7), (-77.5*2, -76.7)]
        for i in positions:
            currpos = (round(self.position[0]+i[0], 1), round(self.position[1]+i[1], 1))
            if ((currpos[0]>=70.5 and currpos[0]<=613) and (currpos[1]>=55.0 and currpos[1]<=591.9)):
                if(not (currpos in board_Info)):
                    moves.append(currpos)           
                else:
                    if(board_Info[currpos].colour != self.colour):
                        moves.append(currpos)
                        #print(self.colour)
                        #print(board_Info[currpos].colour)
        return moves
    
class Queen(Piece):
    def __init__(self, colour, position):
        super().__init__(colour, position)
        self.name = "Queen"
        self.sprite = pygame.transform.smoothscale(pygame.image.load("images/" + colour + "_Queen.png"),(PieceWidth, PieceHeight))
        self.points = 10

    def movement(self, BlackPlayer, WhitePlayer, board_Info):
        pos = []
        temp_Rook = Rook(self.colour, self.position)
        temp_Bishop = Bishop(self.colour, self.position)
        pos.extend(temp_Rook.movement(BlackPlayer, WhitePlayer, board_Info))
        pos.extend(temp_Bishop.movement(BlackPlayer, WhitePlayer, board_Info))
        return pos

class King(Piece):
    def __init__(self, colour, position):
        super().__init__(colour, position)
        self.name = "King"
        self.sprite = pygame.transform.smoothscale(pygame.image.load("images/" + colour + "_King.png"),(PieceWidth, PieceHeight))
        self.points = 200

    def movement(self, BlackPlayer, WhitePlayer, board_Info, recursion):
        moves = []
        xvalues = [(-1)*hshift, 0, hshift]
        yvalues = [(-1)*vshift, 0, vshift]
        for i in xvalues:
            for j in yvalues:
                currpos = (round(self.position[0]+i, 1), round(self.position[1]+j, 1))
                if currpos != self.position:
                    if ((currpos[0]>=70.5 and currpos[0]<=613) and (currpos[1]>=55.0 and currpos[1]<=591.9)):
                        if(not (currpos in board_Info)):
                            if (recursion == False):
                                if(kingmovehelper(BlackPlayer, WhitePlayer, currpos, self, board_Info) == True):
                                    moves.append(currpos)    
                            else:
                                 moves.append(currpos)       
                        else:
                            if(board_Info[currpos].colour != self.colour):
                                if (recursion == False):
                                    if(kingmovehelper(BlackPlayer, WhitePlayer, currpos, self, board_Info) == True):
                                        moves.append(currpos)
                                else:
                                     moves.append(currpos)
        return moves                






        for i in xvalues:
            for j in yvalues:
                move = (round(self.position[0]+i, 1), round(self.position[1]+j, 1))
                if(50 < move[0] < 650 and 50 < move[1] < 650):
                    if(self.position != move):
                        if(self.colour == "White"):
                            add = True
                            for k in WhitePlayer.pieces:
                                if(move == k.position):
                                    add = False
                                    break
                            if (add == True):
                                if (recursion == False):
                                    if(kingmovehelper(BlackPlayer, WhitePlayer, move, self) == True):
                                            pos.append(move)
                                else:
                                    pos.append(move)
                        
                        if(self.colour == "Black"):
                            add = True
                            for k in BlackPlayer.pieces:
                                if(move == k.position):
                                    add = False
                                    break
                            if (add == True):
                                if(recursion == False):
                                    if(kingmovehelper(BlackPlayer, WhitePlayer, move, self) == True):
                                        pos.append(move)
                                else:
                                    pos.append(move)
        return pos

def kingmovehelper(BlackPlayer, WhitePlayer, new_pos, king, board_Info):
    """
        Helper for king movement, depicts if king's move will collide in the path of any of the opponents pieces movement.
        Returns true if safe for king to move there.
    """
    piece_holder=None
    if king.colour == "Black":
        player=BlackPlayer
        otherplayer=WhitePlayer
    else:
        player=WhitePlayer
        otherplayer=BlackPlayer
    temp_piece = Pawn(king.colour, new_pos)
    if(new_pos in board_Info):
        piece_holder = board_Info[new_pos]
        otherplayer.pieces.remove(piece_holder)
    board_Info[new_pos]= temp_piece
    player.pieces.append(temp_piece)
    for i in otherplayer.pieces:
        if i.name == "King":
            if new_pos in i.movement(BlackPlayer, WhitePlayer, board_Info, True):
                player.pieces.remove(temp_piece)
                if piece_holder!=None:
                    otherplayer.pieces.append(piece_holder)
                    board_Info[new_pos] = piece_holder
                else:
                    board_Info.pop(new_pos)
                return False
        else:
            if new_pos in i.movement(BlackPlayer, WhitePlayer, board_Info):
                player.pieces.remove(temp_piece)
                if piece_holder!=None:
                    otherplayer.pieces.append(piece_holder)
                    board_Info[new_pos] = piece_holder
                else:
                    board_Info.pop(new_pos)
                return False
    if piece_holder != None:
        player.pieces.remove(temp_piece)
        otherplayer.pieces.append(piece_holder)
        board_Info[new_pos] = piece_holder
    else:
        player.pieces.remove(temp_piece)
        board_Info.pop(new_pos)

    return True












    temp_remove = None
    #check if king kills a piece will it put it in check, which is an illegal move
    if (king.colour == "White"):
        for i in BlackPlayer.pieces:
            if(i.position == new_pos): #checks if any enemy piece is on moving position
                temp_remove = i
                BlackPlayer.pieces.remove(i) #removes it for the sake of 
                break

        #check if p
        for i in BlackPlayer.pieces:
            if(i.name == "Pawn"):
                if(round(i.position[0]-hshift, 1) == new_pos[0] and round(i.position[1]+vshift, 1) == new_pos[1]): #Pawn left diag kill
                    if(temp_remove != None):
                        BlackPlayer.pieces.append(temp_remove)
                    return False
                if(round(i.position[0]+hshift, 1) == new_pos[0] and round(i.position[1]+vshift, 1) == new_pos[1]): #Pawn right diag kill
                    if(temp_remove != None):
                        BlackPlayer.pieces.append(temp_remove)
                    return False
            elif(i.name == "King"):
                for j in i.movement(BlackPlayer, WhitePlayer, board_Info, True):
                    if (j[0]==new_pos[0] and j[1]==new_pos[1]):
                        if(temp_remove!=None):
                            BlackPlayer.pieces.append(temp_remove)
                        return False
            else:
                currPos = king.position
                king.position = new_pos
                for j in i.movement(BlackPlayer, WhitePlayer, board_Info):
                    if (j[0]==new_pos[0] and j[1]==new_pos[1]):
                        if(temp_remove!=None):
                            BlackPlayer.pieces.append(temp_remove)
                        king.position = currPos
                        return False
                king.position = currPos
        if(temp_remove!=None):
            BlackPlayer.pieces.append(temp_remove)

    if (king.colour == "Black"):
        for i in WhitePlayer.pieces:
            if(i.position == new_pos):
                temp_remove = i
                WhitePlayer.pieces.remove(i)
                break
        for i in WhitePlayer.pieces:
            if(i.name == "Pawn"):
                if(round(i.position[0]-hshift, 1) == new_pos[0] and round(i.position[1]-vshift, 1) == new_pos[1]):
                    if(temp_remove != None):
                        WhitePlayer.pieces.append(temp_remove)
                    return False
                if(round(i.position[0]+hshift, 1) == new_pos[0] and round(i.position[1]-vshift, 1) == new_pos[1]):
                    if(temp_remove != None):
                        WhitePlayer.pieces.append(temp_remove)
                    return False
            elif(i.name == "King"):
                for j in i.movement(BlackPlayer, WhitePlayer, board_Info, True):
                    if (j[0]==new_pos[0] and j[1]==new_pos[1]):
                        if(temp_remove!=None):
                           WhitePlayer.pieces.append(temp_remove)
                        return False
            else:
                currPos = king.position
                king.position = new_pos
                for j in i.movement(BlackPlayer, WhitePlayer, board_Info):
                    if (j[0]==new_pos[0] and j[1]==new_pos[1]):
                        if(temp_remove!=None):
                            WhitePlayer.pieces.append(temp_remove)
                        king.position = currPos
                        return False
                king.position = currPos
        if(temp_remove!=None):
            WhitePlayer.pieces.append(temp_remove)
    return True