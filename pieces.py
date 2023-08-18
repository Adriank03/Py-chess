import pygame

hshift, vshift = 77.5, 76.7
PieceWidth, PieceHeight = 80, 80

class Piece():
    def __init__(self, colour, position):
        self.colour = colour
        self.position = position
        

    def movement(self, BlackPlayer, WhitePlayer):
        """
            Abstract method, should return pieces unique movement.
        """
        return []

class Pond(Piece):
    def __init__(self, colour, position):
        super().__init__(colour, position)
        self.name = "Pond"
        self.sprite = pygame.transform.scale(pygame.image.load("images/" + colour + "_Pond.png"),(PieceWidth, PieceHeight))
        self.points = 1
    
    def movement(self, BlackPlayer, WhitePlayer):
        pos = []
        blocked = False
        #for the white pond
        if (self.colour == "White"):
            shiftedy=round(self.position[1]-76.7, 1)
            for i in BlackPlayer.pieces:
                if(round(self.position[0]-77.5, 1) == i.position[0] and shiftedy == i.position[1]):#diagonal
                    pos.append(i.position)
                if(round(self.position[0]+77.5, 1) == i.position[0] and shiftedy == i.position[1]):#diagonal
                    pos.append(i.position)
                if(self.position[0] == i.position[0] and shiftedy == i.position[1]):#black piece blocking
                    blocked = True
            if (blocked == False): 
                for i in WhitePlayer.pieces:
                    if(self.position[0] == i.position[0] and shiftedy == i.position[1]): #if white piece is blocking
                        blocked = True
                        break
            if (blocked == False): #if no pieces are blocking
                if(self.position[1]-76.7 > 50): #bounds of board
                    pos.append((self.position[0], shiftedy)) 

        if (self.colour == "Black"):
            shiftedy=round(self.position[1]+76.7, 1)
            for i in WhitePlayer.pieces:
                if(round(self.position[0]-77.5, 1) == i.position[0] and shiftedy == i.position[1]):#diagonal
                    pos.append(i.position)
                if(round(self.position[0]+77.5, 1) == i.position[0] and shiftedy == i.position[1]):#diagonal
                    pos.append(i.position)
                if(self.position[0] == i.position[0] and shiftedy == i.position[1]):#white piece blocking
                    blocked = True
            if (blocked == False): 
                for i in BlackPlayer.pieces:
                    if(self.position[0] == i.position[0] and shiftedy == i.position[1]): #if white piece is blocking
                        blocked = True
                        break
            if (blocked == False): #if no pieces are blocking
                if(self.position[1]-76.7 > 50): #bounds of board
                    pos.append((self.position[0], shiftedy)) 
        return pos

class Rook(Piece):
    def __init__(self, colour, position):
        super().__init__(colour, position)
        self.name = "Rook"
        self.sprite = pygame.transform.scale(pygame.image.load("images/" + colour + "_Rook.png"),(PieceWidth, PieceHeight))
        self.points = 5

    def movement(self, BlackPlayer, WhitePlayer):
        pos = []

        #up
        i=1
        blocked = 0
        while(i<8):
            shiftedy = round(self.position[1]-(76.7*i), 1)
            if (shiftedy < 50):
                i+=10
                break
            for j in BlackPlayer.pieces:
                if(self.position[0] == j.position[0] and shiftedy == j.position[1]):
                    if(self.colour == "White"):
                        pos.append((self.position[0], shiftedy))
                    i+=10
                    blocked+=1
                    break
            if(blocked == 0):
                for j in WhitePlayer.pieces:
                    if(self.position[0] == j.position[0] and shiftedy == j.position[1]):
                        if(self.colour == "Black"):
                            pos.append((self.position[0], shiftedy))
                        blocked+=1
                        i+=10
                        break
            if(blocked == 0):
                pos.append((self.position[0],shiftedy))
            i+=1

        #down
        i=1
        blocked = 0
        while(i<8):
            shiftedy = round(self.position[1]+(76.7*i), 1)
            if (shiftedy > 650):
                i+=10
                break
            for j in BlackPlayer.pieces:
                if(self.position[0] == j.position[0] and shiftedy == j.position[1]):
                    if(self.colour == "White"):
                        pos.append((self.position[0], shiftedy))
                    i+=10
                    blocked+=1
                    break
            if(blocked == 0):
                for j in WhitePlayer.pieces:
                    if(self.position[0] == j.position[0] and shiftedy == j.position[1]):
                        if(self.colour == "Black"):
                            pos.append((self.position[0], shiftedy))
                        blocked+=1
                        i+=10
                        break
            if(blocked == 0):
                pos.append((self.position[0],shiftedy))
            i+=1

        #left
        i=1
        blocked = 0
        while(i<8):
            shiftedx = round(self.position[0]-(77.5*i), 1)
            if (shiftedx < 50):
                i+=10
                break
            for j in BlackPlayer.pieces:
                if(shiftedx == j.position[0] and self.position[1] == j.position[1]):
                    if(self.colour == "White"):
                        pos.append((shiftedx, self.position[1]))
                    i+=10
                    blocked+=1
                    break
            if(blocked == 0):
                for j in WhitePlayer.pieces:
                    if(shiftedx == j.position[0] and self.position[1] == j.position[1]):
                        if(self.colour == "Black"):
                            pos.append((shiftedx, self.position[1]))
                        blocked+=1
                        i+=10
                        break
            if(blocked == 0):
                pos.append((shiftedx, self.position[1]))
            i+=1

        #right
        i=1
        blocked = 0
        while(i<8):
            shiftedx = round(self.position[0]+(77.5*i), 1)
            if (shiftedx > 650):
                i+=10
                break
            for j in BlackPlayer.pieces:
                if(shiftedx == j.position[0] and self.position[1] == j.position[1]):
                    if(self.colour == "White"):
                        pos.append((shiftedx, self.position[1]))
                    i+=10
                    blocked+=1
                    break
            if(blocked == 0):
                for j in WhitePlayer.pieces:
                    if(shiftedx == j.position[0] and self.position[1] == j.position[1]):
                        if(self.colour == "Black"):
                            pos.append((shiftedx, self.position[1]))
                        blocked+=1
                        i+=10
                        break
            if(blocked == 0):
                pos.append((shiftedx, self.position[1]))
            i+=1

        return pos
    
class Bishop(Piece):
    def __init__(self, colour, position):
        super().__init__(colour, position)
        self.name = "Bishop"
        self.sprite = pygame.transform.scale(pygame.image.load("images/" + colour + "_Bishop.png"),(PieceWidth, PieceHeight))
        self.points = 3

    def movement(self, BlackPlayer, WhitePlayer):
        pos = []
        i=1
        stopupleft = False
        stopupright = False
        stopdownleft = False
        stopdownright = False

        while(i<8):
            #upleft
            shiftedx1 = round(self.position[0]-(77.5*i), 1)
            shiftedy1 = round(self.position[1]-(76.7*i), 1)
            #upright
            shiftedx2 = round(self.position[0]+(77.5*i), 1)
            shiftedy2 = round(self.position[1]-(76.7*i), 1)
            #downleft
            shiftedx3 = round(self.position[0]-(77.5*i), 1)
            shiftedy3 = round(self.position[1]+(76.7*i), 1)
            #downright
            shiftedx4 = round(self.position[0]+(77.5*i), 1)
            shiftedy4 = round(self.position[1]+(76.7*i), 1)

            #check
            for j in BlackPlayer.pieces: 
                if(shiftedx1 == j.position[0] and shiftedy1 == j.position[1]):
                    if(self.colour == "White" and stopupleft == False):
                        pos.append((shiftedx1, shiftedy1))
                    stopupleft = True
                if(shiftedx2 == j.position[0] and shiftedy2 == j.position[1]):
                    if(self.colour == "White" and stopupright == False):
                        pos.append((shiftedx2, shiftedy2))
                    stopupright = True
                if(shiftedx3 == j.position[0] and shiftedy3 == j.position[1]):
                    if(self.colour == "White" and stopdownleft == False):
                        pos.append((shiftedx3, shiftedy3))
                    stopdownleft = True
                if(shiftedx4 == j.position[0] and shiftedy4 == j.position[1]):
                    if(self.colour == "White" and stopdownright == False):
                        pos.append((shiftedx4, shiftedy4))
                    stopdownright = True

            for j in WhitePlayer.pieces: 
                if(shiftedx1 == j.position[0] and shiftedy1 == j.position[1]):
                    if(self.colour == "Black" and stopupleft == False):
                        pos.append((shiftedx1, shiftedy1))
                    stopupleft = True
                if(shiftedx2 == j.position[0] and shiftedy2 == j.position[1]):
                    if(self.colour == "Black" and stopupright == False):
                        pos.append((shiftedx2, shiftedy2))
                    stopupright = True
                if(shiftedx3 == j.position[0] and shiftedy3 == j.position[1]):
                    if(self.colour == "Black" and stopdownleft == False):
                        pos.append((shiftedx3, shiftedy3))
                    stopdownleft = True
                if(shiftedx4 == j.position[0] and shiftedy4 == j.position[1]):
                    if(self.colour == "Black" and stopdownright == False):
                        pos.append((shiftedx4, shiftedy4))
                    stopdownright = True

            if(stopupleft == False):
                if(shiftedx1 > 50 and shiftedy1 > 50):
                    pos.append((shiftedx1,shiftedy1))
            if(stopupright == False):
                if(shiftedx2 < 650 and shiftedy2 > 50):
                    pos.append((shiftedx2,shiftedy2))
            if(stopdownleft == False):
                if(shiftedx3 > 50 and shiftedy3 < 650):
                    pos.append((shiftedx3,shiftedy3))
            if(stopdownright == False):
                if(shiftedx4 < 650 and shiftedy4 < 650):
                    pos.append((shiftedx4,shiftedy4))
            i+=1

        return pos
    
class Knight(Piece):
    def __init__(self, colour, position):
        super().__init__(colour, position)
        self.name = "Knight"
        self.sprite = pygame.transform.scale(pygame.image.load("images/" + colour + "_Knight.png"),(PieceWidth, PieceHeight))
        self.points = 3

    def movement(self, BlackPlayer, WhitePlayer):
        pos = []

        shiftedpos = {
        #upleft
        "shiftedx1" : round(self.position[0]-(77.5), 1),
        "shiftedy1" : round(self.position[1]-(76.7*2), 1),
        #upright
        "shiftedx2" : round(self.position[0]+(77.5), 1),
        "shiftedy2" : round(self.position[1]-(76.7*2), 1),
        #rightup
        "shiftedx3" : round(self.position[0]+(77.5*2), 1),
        "shiftedy3" : round(self.position[1]-(76.7), 1),
        #rightdown
        "shiftedx4" : round(self.position[0]+(77.5*2), 1),
        "shiftedy4" : round(self.position[1]+(76.7), 1),
        #downright
        "shiftedx5" : round(self.position[0]+(77.5), 1),
        "shiftedy5" : round(self.position[1]+(76.7*2), 1),
        #downleft
        "shiftedx6" : round(self.position[0]-(77.5), 1),
        "shiftedy6" : round(self.position[1]+(76.7*2), 1),
        #leftdown
        "shiftedx7" : round(self.position[0]-(77.5*2), 1),
        "shiftedy7" : round(self.position[1]+(76.7), 1),
        #leftup
        "shiftedx8" : round(self.position[0]-(77.5*2), 1),
        "shiftedy8" : round(self.position[1]-(76.7), 1)
        }
        if(self.colour == "Black"):
            for j in range(1,9):
                add = True
                for i in BlackPlayer.pieces:
                    if (shiftedpos["shiftedx"+str(j)] == i.position[0] and shiftedpos["shiftedy"+str(j)] == i.position[1]):
                        add = False
                        break
                if (add==True):
                    if(50 < shiftedpos["shiftedx"+str(j)] < 650 and 50 < shiftedpos["shiftedy"+str(j)] < 650):
                        pos.append((shiftedpos["shiftedx"+str(j)],shiftedpos["shiftedy"+str(j)]))

        if(self.colour == "White"):
            for j in range(1,9):
                add = True
                for i in WhitePlayer.pieces:
                    if (shiftedpos["shiftedx"+str(j)] == i.position[0] and shiftedpos["shiftedy"+str(j)] == i.position[1]):
                        add = False
                        break
                if (add==True):
                    if(50 < shiftedpos["shiftedx"+str(j)] < 650 and 50 < shiftedpos["shiftedy"+str(j)] < 650):
                        pos.append((shiftedpos["shiftedx"+str(j)],shiftedpos["shiftedy"+str(j)]))
        return pos
    
class Queen(Piece):
    def __init__(self, colour, position):
        super().__init__(colour, position)
        self.name = "Queen"
        self.sprite = pygame.transform.scale(pygame.image.load("images/" + colour + "_Queen.png"),(PieceWidth, PieceHeight))
        self.points = 10

    def movement(self, BlackPlayer, WhitePlayer):
        pos = []
        temp_Rook = Rook(self.colour, self.position)
        temp_Bishop = Bishop(self.colour, self.position)
        pos.extend(temp_Rook.movement(BlackPlayer, WhitePlayer))
        pos.extend(temp_Bishop.movement(BlackPlayer, WhitePlayer))
        return pos

class King(Piece):
    def __init__(self, colour, position):
        super().__init__(colour, position)
        self.name = "King"
        self.sprite = pygame.transform.scale(pygame.image.load("images/" + colour + "_King.png"),(PieceWidth, PieceHeight))
        self.points = 200

    def movement(self, BlackPlayer, WhitePlayer, recursion):
        pos = []
        xvalues = [(-1)*hshift, 0, hshift]
        yvalues = [(-1)*vshift, 0, vshift]
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

def kingmovehelper(BlackPlayer, WhitePlayer, new_pos, king):
    """
        Helper for king movement, depicts if king's move will collide in the path of any of the opponents pieces movement.
        Returns true if safe for king to move there.
    """
    temp_remove = None
    if (king.colour == "White"):
        for i in BlackPlayer.pieces:
            if(i.position == new_pos):
                temp_remove = i
                BlackPlayer.pieces.remove(i)
                break
        for i in BlackPlayer.pieces:
            if(i.name == "King"):
                for j in i.movement(BlackPlayer, WhitePlayer, True):
                    if (j[0]==new_pos[0] and j[1]==new_pos[1]):
                        if(temp_remove!=None):
                            BlackPlayer.pieces.append(temp_remove)
                        return False
            else:
                for j in i.movement(BlackPlayer, WhitePlayer):
                    if (j[0]==new_pos[0] and j[1]==new_pos[1]):
                        if(temp_remove!=None):
                            BlackPlayer.pieces.append(temp_remove)
                        return False
        if(temp_remove!=None):
            BlackPlayer.pieces.append(temp_remove)
                
    if (king.colour == "Black"):
        for i in WhitePlayer.pieces:
            if(i.position == new_pos):
                temp_remove = i
                WhitePlayer.pieces.remove(i)
                break
        for i in WhitePlayer.pieces:
            if(i.name == "King"):
                for j in i.movement(BlackPlayer, WhitePlayer, True):
                    if (j[0]==new_pos[0] and j[1]==new_pos[1]):
                        if(temp_remove!=None):
                           WhitePlayer.pieces.append(temp_remove)
                        return False
            else:
                for j in i.movement(BlackPlayer, WhitePlayer):
                    if (j[0]==new_pos[0] and j[1]==new_pos[1]):
                        if(temp_remove!=None):
                            WhitePlayer.pieces.append(temp_remove)
                        return False
        if(temp_remove!=None):
            WhitePlayer.pieces.append(temp_remove)
    return True