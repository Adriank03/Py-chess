import pygame
import math
from button import *
pygame.init()

font = pygame.font.Font("font.ttf", 40)
font2 = pygame.font.Font("font.ttf", 23)
font3 = pygame.font.Font("font.ttf", 19)

global offset

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
    hovering.activate(WIN, None)


def mainMenu(WIN):
    global offset
    text = font2.render("Play Game", True, (255,255,255))
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
        
        buttons = [Button("Start", (255, 255, 255), (210,180,140), (181,136,99), (120, 50), (315, 550))]
    
        blackScreen.set_alpha(120)
        while(start == False):
            offset=0
            while(offset<1000 and start2 == False):
                hovering = None
                width += math.sin(offset/20) * 1.5
                height += math.sin(offset/20) * 1.5
                logo = pygame.transform.smoothscale(pygame.image.load("images/logo.png"),(width, height))
                rect = logo.get_rect(center = rect.center)
                offset+=1
                pos = pygame.mouse.get_pos()
                WIN.blit(board, (-75,-offset))
                WIN.blit(board, (-75,1000 -offset))
                WIN.blit(blackScreen, (0,0))
                req = buttons[0].check_hover(pos)
                if(req != None):
                    hovering = req
                buttons[0].draw_button(WIN)
                WIN.blit(text, (323, 560))
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
    
    tanRecScale = pygame.transform.scale(pygame.image.load("images/tan_rec.png"),(width, height))
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
        tanRecScale = pygame.transform.smoothscale(pygame.image.load("images/tan_rec.png"),(width, height))
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
            
