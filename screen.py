import pygame
import math
from button import *
from DB import *


pygame.init()

font = pygame.font.Font("font.ttf", 40)
font2 = pygame.font.Font("font.ttf", 23)
font3 = pygame.font.Font("font.ttf", 19)
font4 = pygame.font.Font("font.ttf", 17)
font5 = pygame.font.Font("font.ttf", 30)

global offset
loggedin = None

def chooseDiff(WIN):
    global offset
    text = font2.render("No Bot", True, (255,255,255))
    text2 = font2.render("Noob", True, (255,255,255))
    text3 = font2.render("Smart", True, (255,255,255))
    choose = False
    start = False
    start2 = False
    while(choose == False):
        blackScreen = pygame.transform.scale(pygame.image.load("images/blackScreen.jpeg"),(1000, 1000))
        board = pygame.transform.smoothscale(pygame.image.load("images/board2.png"),(1000, 1000))
        
        buttons = [Button("No Bot", (255, 255, 255), (210,180,140), (181,136,99), (120, 50), (120, 550)),
                   Button("Noob", (255, 255, 255), (210,180,140), (181,136,99), (120, 50), (320, 550)),
                   Button("Smart", (255, 255, 255), (210,180,140), (181,136,99), (120, 50), (520, 550))]

        blackScreen.set_alpha(120)
        while(start == False):
            while(offset<1000 and start2 == False):
                hovering = None
                offset+=1
                pos = pygame.mouse.get_pos()
                WIN.blit(board, (-75,-offset))
                WIN.blit(board, (-75,1000 -offset))
                WIN.blit(blackScreen, (0,0))
                for i in buttons:
                    req = i.check_hover(pos)
                    if(req != None):
                        hovering = req
                    i.draw_button(WIN)
                WIN.blit(text, (145, 560))
                WIN.blit(text2, (353, 560))
                WIN.blit(text3, (554, 560))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if hovering!= None:
                            choose = True
                            start = True
                            start2 = True
                            break
                pygame.display.update()
    loggedin = False
    hovering.activate(WIN, None)


def mainMenu(WIN):
    global offset
    global loggedin

    text = font3.render("Single Player", True, (255,255,255))
    text2 = font3.render("Online", True, (255,255,255))
    width = 450
    height = 450
    x= 150
    y= 40
    hovering = None
    choose = False
    start = False
    start2 = False
    while(choose == False):
        blackScreen = pygame.transform.scale(pygame.image.load("images/blackScreen.jpeg"),(1000, 1000))
        board = pygame.transform.smoothscale(pygame.image.load("images/board2.png"),(1000, 1000))
        logo = pygame.transform.scale(pygame.image.load("images/logo.png"),(width, height))
        rect = logo.get_rect(topleft = (x, y))
        
        buttons = [Button("Start", (255, 255, 255), (210,180,140), (181,136,99), (120, 50), (315, 550)),
                   Button("Online", (255, 255, 255), (210,180,140), (181,136,99), (120, 50), (315, 620))]
    
        blackScreen.set_alpha(120)
        while(start == False):
            offset=0
            while(offset<1000 and start2 == False):
                hovering = None
                width += math.sin(offset/20) * 1.5
                height += math.sin(offset/20) * 1.5
                logo = pygame.transform.smoothscale(pygame.image.load("images/logo.png"),(int(width), int(height)))
                rect = logo.get_rect(center = rect.center)
                offset+=1
                pos = pygame.mouse.get_pos()
                WIN.blit(board, (-75,-offset))
                WIN.blit(board, (-75,1000 -offset))
                WIN.blit(blackScreen, (0,0))
                for i in buttons:
                    req = i.check_hover(pos)
                    if(req != None):
                        hovering = req
                    i.draw_button(WIN)
                buttons[0].draw_button(WIN)
                buttons[1].draw_button(WIN)
                WIN.blit(text, (324, 563))
                WIN.blit(text2, (349, 633))
                WIN.blit(logo, rect)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if hovering!= None:
                            print(hovering)
                            choose = True
                            start = True
                            start2 = True
                            break
                pygame.display.update()
    if hovering!= None:
        hovering.activate(WIN, None)

def loginscreen1(WIN):
    from client import playOnline
    global offset
    uname = ''
    message = ''
    title = font5.render("Username:", True, (255,255,255))
    text2 = font3.render("Go", True, (255,255,255))
    choose = False
    start = False
    start2 = False
    while(choose == False):
        blackScreen = pygame.transform.scale(pygame.image.load("images/blackScreen.jpeg"),(1000, 1000))
        board = pygame.transform.smoothscale(pygame.image.load("images/board2.png"),(1000, 1000))
        
        Go = Button("Go", (255, 255, 255), (210,180,140), (181,136,99), (45, 50), (550, 350))
        usernamebar = Button("usernamebar", (255, 255, 255), (210,180,140), (181,136,99), (300, 50), (200, 350))

        blackScreen.set_alpha(120)
        while(start == False):
            while(offset<1000 and start2 == False):
                username = font2.render(uname, True, (255, 255, 255))
                msg = font2.render(message, True, (255, 255, 255))
                hovering = None
                offset+=1
                pos = pygame.mouse.get_pos()
                WIN.blit(board, (-75,-offset))
                WIN.blit(board, (-75,1000 -offset))
                WIN.blit(blackScreen, (0,0))
                req = Go.check_hover(pos)
                if(req != None):
                    hovering = req
                Go.draw_button(WIN)
                usernamebar.draw_button(WIN)
                WIN.blit(title, (200, 300))
                WIN.blit(username, (225, 360))
                WIN.blit(text2, (561, 364))
                WIN.blit(msg, (200, 410))

                for event in pygame.event.get():

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            if len(uname)>0:
                                uname = uname[0:-1]
                        else:
                            if event.unicode.isalnum() and len(uname) < 16:
                                uname += event.unicode
                    elif event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if hovering!= None:
                            found = 0
                            dbname = findUser(uname)
                            for i in dbname:
                                found += 1
                                userinfo = i
                            if found > 0:
                                choose = True
                                start = True
                                start2 = True
                                break
                            else:
                                message = "Username Not Found"
                pygame.display.update()
    pword = ''
    hidden = ''
    message = ''
    title = font5.render("Enter Password", True, (255,255,255))
    title2 = font5.render("User: "+ uname, True, (255,255,255))
    text2 = font3.render("Go", True, (255,255,255))
    choose = False
    start = False
    start2 = False
    while(choose == False):
        blackScreen = pygame.transform.scale(pygame.image.load("images/blackScreen.jpeg"),(1000, 1000))
        board = pygame.transform.smoothscale(pygame.image.load("images/board2.png"),(1000, 1000))
        
        Go = Button("Go", (255, 255, 255), (210,180,140), (181,136,99), (45, 50), (550, 350))
        passwordbar = Button("passwordbar", (255, 255, 255), (210,180,140), (181,136,99), (300, 50), (200, 350))

        blackScreen.set_alpha(120)
        while(start == False):
            while(offset<1000 and start2 == False):
                password = font2.render(hidden, True, (255, 255, 255))
                msg = font2.render(message, True, (255, 255, 255))
                hovering = None
                offset+=1
                pos = pygame.mouse.get_pos()
                WIN.blit(board, (-75,-offset))
                WIN.blit(board, (-75,1000 -offset))
                WIN.blit(blackScreen, (0,0))
                req = Go.check_hover(pos)
                if(req != None):
                    hovering = req
                Go.draw_button(WIN)
                passwordbar.draw_button(WIN)
                WIN.blit(title, (200, 270))
                WIN.blit(title2, (200, 300))
                WIN.blit(password, (225, 360))
                WIN.blit(text2, (561, 364))
                WIN.blit(msg, (200, 410))

                for event in pygame.event.get():

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            if len(pword)>0:
                                pword = pword[0:-1]
                                hidden = hidden[0:-1]
                        else:
                            if event.unicode.isalnum() and len(pword) < 16:
                                pword += event.unicode
                                hidden += '*'
                    elif event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if hovering!= None:
                            found = 0
                            if pword == userinfo[1]:
                                choose = True
                                start = True
                                start2 = True
                                break
                            else:
                                message = "Password Does Not Match This Account"
                pygame.display.update()
    playOnline(WIN)



def createAccountScreen1(WIN):
    global offset
    uname = ''
    message = ''
    title = font5.render("Choose Your Username", True, (255,255,255))
    text2 = font3.render("Go", True, (255,255,255))
    choose = False
    start = False
    start2 = False
    while(choose == False):
        blackScreen = pygame.transform.scale(pygame.image.load("images/blackScreen.jpeg"),(1000, 1000))
        board = pygame.transform.smoothscale(pygame.image.load("images/board2.png"),(1000, 1000))
        
        Go = Button("Go", (255, 255, 255), (210,180,140), (181,136,99), (45, 50), (550, 350))
        usernamebar = Button("usernamebar", (255, 255, 255), (210,180,140), (181,136,99), (300, 50), (200, 350))

        blackScreen.set_alpha(120)
        while(start == False):
            while(offset<1000 and start2 == False):
                username = font2.render(uname, True, (255, 255, 255))
                msg = font2.render(message, True, (255, 255, 255))
                hovering = None
                offset+=1
                pos = pygame.mouse.get_pos()
                WIN.blit(board, (-75,-offset))
                WIN.blit(board, (-75,1000 -offset))
                WIN.blit(blackScreen, (0,0))
                req = Go.check_hover(pos)
                if(req != None):
                    hovering = req
                Go.draw_button(WIN)
                usernamebar.draw_button(WIN)
                WIN.blit(title, (200, 300))
                WIN.blit(username, (215, 360))
                WIN.blit(text2, (561, 364))
                WIN.blit(msg, (200, 410))

                for event in pygame.event.get():

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            if len(uname)>0:
                                uname = uname[0:-1]
                        else:
                            if event.unicode.isalnum() and len(uname) < 16:
                                uname += event.unicode
                    elif event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if hovering!= None:
                            if len(uname) >= 4:
                                found = 0
                                dbname = findUser(uname)
                                for i in dbname:
                                    found += 1
                                if found > 0:
                                    message = "Username already in use"
                                else:
                                    choose = True
                                    start = True
                                    start2 = True
                                    loggedin= (uname, pword)
                                    break
                                    
                            else:
                                message = "Username must have mininum 4 characters"
                pygame.display.update()
    pword = ''
    hidden = ''
    message = ''
    title = font5.render("Choose A Password", True, (255,255,255))
    title2 = font5.render("User: "+uname, True, (255,255,255))
    text2 = font3.render("Go", True, (255,255,255))
    choose = False
    start = False
    start2 = False
    while(choose == False):
        blackScreen = pygame.transform.scale(pygame.image.load("images/blackScreen.jpeg"),(1000, 1000))
        board = pygame.transform.smoothscale(pygame.image.load("images/board2.png"),(1000, 1000))
        
        Go = Button("Go", (255, 255, 255), (210,180,140), (181,136,99), (45, 50), (550, 350))
        passwordbar = Button("passwordbar", (255, 255, 255), (210,180,140), (181,136,99), (300, 50), (200, 350))

        blackScreen.set_alpha(120)
        while(start == False):
            while(offset<1000 and start2 == False):
                password = font2.render(hidden, True, (255, 255, 255))
                msg = font2.render(message, True, (255, 255, 255))
                hovering = None
                offset+=1
                pos = pygame.mouse.get_pos()
                WIN.blit(board, (-75,-offset))
                WIN.blit(board, (-75,1000 -offset))
                WIN.blit(blackScreen, (0,0))
                req = Go.check_hover(pos)
                if(req != None):
                    hovering = req
                Go.draw_button(WIN)
                passwordbar.draw_button(WIN)
                WIN.blit(title, (200, 270))
                WIN.blit(title2, (200, 300))
                WIN.blit(password, (225, 360))
                WIN.blit(text2, (561, 364))
                WIN.blit(msg, (200, 410))

                for event in pygame.event.get():

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            if len(pword)>0:
                                pword = pword[0:-1]
                                hidden = hidden[0:-1]
                        else:
                            if event.unicode.isalnum() and len(pword) < 16:
                                pword += event.unicode
                                hidden += '*'
                    elif event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if hovering!= None:
                            if len(pword)>0:
                                choose = True
                                start = True
                                start2 = True
                                loggedin = (uname, pword)
                                createUser(loggedin[0], loggedin[1])
                                break
                            else:
                                message = "Password Must Be Atleast One Character"
                pygame.display.update()
    hovering.activate(WIN, None)


def createAccountPhase(WIN):
    global offset
    text = font2.render("Login", True, (255,255,255))
    text2 = font3.render("Create Account", True, (255,255,255))
    text3 = font5.render("Login To An Account to Play", True, (255,255,255))
    choose = False
    start = False
    start2 = False
    while(choose == False):
        blackScreen = pygame.transform.scale(pygame.image.load("images/blackScreen.jpeg"),(1000, 1000))
        board = pygame.transform.smoothscale(pygame.image.load("images/board2.png"),(1000, 1000))
        
        buttons = [Button("Create Account", (255, 255, 255), (210,180,140), (181,136,99), (130, 50), (315, 350)),
                   Button("Login", (255, 255, 255), (210,180,140), (181,136,99), (130, 50), (315, 420))]

        blackScreen.set_alpha(120)
        while(start == False):
            while(offset<1000 and start2 == False):
                hovering = None
                offset+=1
                pos = pygame.mouse.get_pos()
                WIN.blit(board, (-75,-offset))
                WIN.blit(board, (-75,1000 -offset))
                WIN.blit(blackScreen, (0,0))
                for i in buttons:
                    req = i.check_hover(pos)
                    if(req != None):
                        hovering = req
                    i.draw_button(WIN)
                WIN.blit(text3, (210, 250))
                WIN.blit(text2, (322, 362))
                WIN.blit(text, (351, 430))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if hovering!= None:
                            choose = True
                            start = True
                            start2 = True
                            break
                pygame.display.update()
    hovering.activate(WIN, None)
    

def endScreen(WIN, checkMate, WhitePlayersTurn, diff):
    if(checkMate == True):
        status = "CHECKMATE"
        if(WhitePlayersTurn):
            Winner = "White"
        else:
            Winner = "Black"
    else:
        status = "STALEMATE"
        if(WhitePlayersTurn):
            Winner = "Black"
        else:
            Winner = "White"
    
    alpha = 1
    velocity = 1
    x = 375
    y = 375
    width = 0.1
    height = 0.1
    blackScreen = pygame.transform.scale(pygame.image.load("images/blackScreen.jpeg"),(1000, 1000))
    
    tanRecScale = pygame.transform.scale(pygame.image.load("images/tan_rec.png"),(int(width), int(height)))
    rect = tanRecScale.get_rect(topleft = (x, y))

    blackScreen.set_alpha(alpha)
    for i in range(80):
        velocity += 0.0011
        alpha *= velocity
        blackScreen.set_alpha(alpha)
        WIN.blit(blackScreen, (0,0))
        pygame.display.update()
    velocity = 0
    diff = 1
    drop = True
    accel = 0.00001
    while(width < 350):
        if(width > 200):
            drop = False
        if(drop == True):
            accel *= 1.28
            velocity += accel
        if(drop == False):
            if(velocity <= 0.5):
                velocity = 0.5
            velocity /= 1.33
        width += velocity
        height += velocity
        tanRecScale = pygame.transform.smoothscale(pygame.image.load("images/tan_rec.png"),(int(width), int(height)))
        rect = tanRecScale.get_rect(center = rect.center)
        WIN.blit(tanRecScale, rect)
        pygame.display.update()
    alpha = 255
    buttons = [Button("play again", (255, 255, 255), (210,180,140), (181,136,99), (120, 50), (235, 390)),
               Button("main menu", (255, 255, 255), (210,180,140), (181,136,99), (120, 50), (400, 390))]
    while(alpha >0):
        mouse_pos = pygame.mouse.get_pos()
        alpha-= 2
        for i in buttons:
            i.check_hover(mouse_pos)
            i.draw_button(WIN)
        text1=font.render((status), True, (255,255,255))
        text2=font2.render((Winner + " Wins"), True, (255,255,255))
        text3=font3.render(("Play Again"), True, (255,255,255))
        text4=font3.render(("Main Menu"), True, (255,255,255))
        WIN.blit(text1, (255,290))
        WIN.blit(text2, (321,333)) 
        WIN.blit(text3, (253,407)) 
        WIN.blit(text4, (415,407)) 
        
        tanRecScale.set_alpha(alpha)
        WIN.blit(tanRecScale, rect)
        pygame.display.update()
    choose = True
    while(choose == True):
        hovering = None
        for i in buttons:
            mouse_pos = pygame.mouse.get_pos()
            req = i.check_hover(mouse_pos)
            if(req != None):
                hovering = req
            i.draw_button(WIN)  
            WIN.blit(text1, (255,290))
            WIN.blit(text2, (321,333)) 
            WIN.blit(text3, (253,407)) 
            WIN.blit(text4, (415,407))     
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if(hovering != None):
                        choose = False  
                        break        
            pygame.display.update()
    hovering.activate(WIN, diff)   
            