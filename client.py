import socket
from game import *


def playOnline(WIN):
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.connect(("192.168.0.117", 6080))

    colour = serverSocket.recv(2048).decode("utf-8")

    if colour == "White":
        WhitePlayersTurn = True
        num = 1
    else:
        WhitePlayersTurn = False
        num = 2
        
    setUpInfo = setup(num)
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
            if WhitePlayersTurn == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        clicked_pos = pygame.mouse.get_pos()
                        result = choose_piece(WhitePlayer, BlackPlayer, WIN, clicked_pos, WhitePlayersTurn, "online", board_Info)
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
                                                piece = result[1]
                                                movedpos = find_square(clicked_pos)
                                                movestr = str(piece.position[0]) + "," + str(piece.position[1]) + "," + str(movedpos[0]) + "," + str(movedpos[1])
                                                result = move_piece(WhitePlayer, BlackPlayer, WIN, clicked_pos, result[0], result[1], WhitePlayersTurn, board_Info)
                                                if(result == True): # move was mad
                                                    serverSocket.send(bytes(movestr, "utf-8"))
                                                    WhitePlayersTurn = False
                updateboard(WhitePlayer, BlackPlayer, WIN)

            else:
                enemyInfo = serverSocket.recv(2048).decode("utf-8").split(",")
                print(enemyInfo)
                midpointx = 341.75
                midpointy = 323.45

                piecepos = (float(enemyInfo[0]), float(enemyInfo[1]))
                movepos = (float(enemyInfo[2]), float(enemyInfo[3]))

                reflectedpos = (round(midpointx+(midpointx-piecepos[0]), 1), round(midpointy+(midpointy-piecepos[1]), 1))
                reflectedmovepos= (round(midpointx+(midpointx-movepos[0]), 1)+1, round(midpointy+(midpointy-movepos[1]), 1)+1)

                enemypiece = board_Info[reflectedpos]

                if enemypiece.name == "King":
                    result = move_piece(WhitePlayer, BlackPlayer, WIN, reflectedmovepos, enemypiece.movement(BlackPlayer, WhitePlayer, board_Info, False), enemypiece, WhitePlayersTurn, board_Info)
                else:
                    result = move_piece(WhitePlayer, BlackPlayer, WIN, reflectedmovepos, enemypiece.movement(BlackPlayer, WhitePlayer, board_Info), enemypiece, WhitePlayersTurn, board_Info)

                WhitePlayersTurn = True

    endScreen(WIN, checkMate, WhitePlayersTurn, "online")
        
    
