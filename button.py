import pygame

class Button():
    def __init__(self, name, borderColour, innerColour, hovercolour, size, pos):
        self.name = name
        self.borderColour = borderColour
        self.innerColour = innerColour
        self.hoverColour = hovercolour
        self.size = size
        self.pos = pos
        self.currinnercolour = innerColour

    def check_hover(self, mouse_pos):
        if (self.pos[0] < mouse_pos[0] < (self.pos[0]+ self.size[0])) and (self.pos[1] < mouse_pos[1] < (self.pos[1]+ self.size[1])):
            self.currinnercolour = self.hoverColour
            return self
        else:
            self.currinnercolour = self.innerColour
            return None
    
    def draw_button(self, window):
        pygame.draw.rect(window, self.currinnercolour, (self.pos[0], self.pos[1], self.size[0], self.size[1]), border_radius=25)
        pygame.draw.rect(window, self.borderColour, (self.pos[0], self.pos[1], self.size[0], self.size[1]), width=3, border_radius=25)
    
    def playAgain(self, WIN, diff):
        from game import playGame
        print("play again")
        playGame(WIN, diff)
    
    def mainMenu(self, WIN):
        from screen import mainMenu
        print("main menu")
        mainMenu(WIN)
    
    def start(self, WIN):
        from screen import chooseDiff
        chooseDiff(WIN)

    def online(self, WIN):
        from screen import createAccountPhase
        createAccountPhase(WIN)

    def No_Bot(self, WIN):
        self.playAgain(WIN, "No_Bot")

    def Noob(self, WIN):
        self.playAgain(WIN, "Noob")

    def Smart(self, WIN):
        self.playAgain(WIN, "Smart")

    def Create_Account1(self, WIN):
        from screen import createAccountScreen1
        createAccountScreen1(WIN)
    
    def login1(self, WIN):
        from screen import loginscreen1
        loginscreen1(WIN)

    def activate(self, WIN, diff):
        if(self.name == "play again"):
            self.playAgain(WIN, diff)
        elif(self.name == "No Bot"):
            self.No_Bot(WIN)
        elif(self.name == "Noob"):
            self.Noob(WIN)
        elif(self.name == "Smart"):
            self.Smart(WIN)
        elif(self.name == "Start"):
            self.start(WIN)
        elif(self.name == "main menu"):
            self.mainMenu(WIN)
        elif(self.name == "Online"):
            self.online(WIN)
        elif(self.name == "Create Account"):
            self.Create_Account1(WIN)
        elif(self.name == "Login"):
            self.login1(WIN)
