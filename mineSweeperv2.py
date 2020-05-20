### Mine Sweeper

import random
from tkinter import *


class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.buttonArray = [0,0,0,0,0,0,0,0,0],\
                           [0,0,0,0,0,0,0,0,0],\
                           [0,0,0,0,0,0,0,0,0],\
                           [0,0,0,0,0,0,0,0,0],\
                           [0,0,0,0,0,0,0,0,0],\
                           [0,0,0,0,0,0,0,0,0],\
                           [0,0,0,0,0,0,0,0,0],\
                           [0,0,0,0,0,0,0,0,0],\
                           [0,0,0,0,0,0,0,0,0]
        self.checkerArray = [False,False,False,False,False,False,False,False,False,],\
                   [False,False,False,False,False,False,False,False,False,],\
                   [False,False,False,False,False,False,False,False,False,],\
                   [False,False,False,False,False,False,False,False,False,],\
                   [False,False,False,False,False,False,False,False,False,],\
                   [False,False,False,False,False,False,False,False,False,],\
                   [False,False,False,False,False,False,False,False,False,],\
                   [False,False,False,False,False,False,False,False,False,],\
                   [False,False,False,False,False,False,False,False,False,]
        self.bombs = 10
        self.gameOver = 0
        self.create_widgets()
        self.assignBombs()
        
    def create_widgets(self):

        self.instructionsLabel = Label(self, text = "Welcome to Mine Sweeper V1.")
        self.instructionsLabel.grid(row = 0, column = 0, columnspan = 8, sticky = W)

        self.restartButton = Button(self, text = "Start Over", height=4, width=18, bg='black', fg='white', command = lambda: self.restartGame())
        self.restartButton.grid(row = 0, column = 3, columnspan = 3)

        self.notificationLabel = Label(self, text = "Bombs left: 10")
        self.notificationLabel.grid(row = 0, column = 7, columnspan = 4)

        for i in range(len(self.buttonArray)):
            for j in range(len(self.buttonArray[i])):
                self.buttonArray[i][j] = Button(self, text = ' ', height=4, width=8, bg='gray', fg='gray', command = lambda i=i, j=j: self.buttonsClicked(i, j))
                self.buttonArray[i][j].grid(row = i + 8, column = j)

    def restartGame(self):
        for i in range(len(self.buttonArray)):
            for j in range(len(self.buttonArray[i])):
                self.buttonArray[i][j].configure(bg = 'gray', fg = 'gray', state = 'normal')
                self.checkerArray[i][j] = False
        self.instructionsLabel["text"] = "Welcome to Mine Sweeper V1."
        self.gameOver = 0
        self.assignBombs()
        

    def assignBombs(self):
        randomNum = 0
        for i in range(len(self.buttonArray)):
            for j in range(len(self.buttonArray[i])):
                randomNum = random.randint(0,1)
                if(randomNum == 1 and self.bombs > 0):
                    self.buttonArray[i][j]["text"] = "X"
                    self.bombs -= 1
        self.fillBoard()

    def fillBoard(self):
        count = 0
        for i in range(len(self.buttonArray)):
            for j in range(len(self.buttonArray[i])):
                if(self.buttonArray[i][j]["text"] != "X"):
                    if(i > 0 and i < 8 and j > 0 and j < 8 and self.buttonArray[i][j + 1]["text"] == "X"):
                        count += 1
                    if(i > 0 and i < 8 and j > 0 and j < 8 and self.buttonArray[i][j - 1]["text"] == "X"):
                        count += 1
                    if(i > 0 and i < 8 and j > 0 and j < 8 and self.buttonArray[i + 1][j + 1]["text"] == "X"):
                        count += 1
                    if(i > 0 and i < 8 and j > 0 and j < 8 and self.buttonArray[i - 1][j + 1]["text"] == "X"):
                        count += 1
                    if(i > 0 and i < 8 and j > 0 and j < 8 and self.buttonArray[i + 1][j]["text"] == "X"):
                        count += 1
                    if(i > 0 and i < 8 and j > 0 and j < 8 and self.buttonArray[i - 1][j]["text"] == "X"):
                        count += 1
                    if(i > 0 and i < 8 and j > 0 and j < 8 and self.buttonArray[i - 1][j - 1]["text"] == "X"):
                        count += 1
                    if(i > 0 and i < 8 and j > 0 and j < 8 and self.buttonArray[i + 1][j - 1]["text"] == "X"):
                        count += 1
                    if(count == 0):
                        self.buttonArray[i][j]["text"] = " "
                    else:
                        self.buttonArray[i][j]["text"] = str(count)
                    count = 0


    def bombCheck(self, x, y):
        if(x < 0 or y < 0 or x > 8 or y > 8):
            return
        if(self.checkerArray[x][y] == True):
            return
        if(self.buttonArray[x][y]["text"] == ' '):
            self.buttonArray[x][y].configure(fg = 'black', bg = 'white', state = DISABLED)
            self.checkerArray[x][y] = True
            self.bombCheck(x + 1, y)
            self.bombCheck(x + 1, y + 1)
            self.bombCheck(x + 1,y - 1)
            self.bombCheck(x, y - 1)
            self.bombCheck(x, y + 1)
            self.bombCheck(x - 1, y)
            self.bombCheck(x - 1, y - 1)
            self.bombCheck(x - 1,y + 1)
                
    def disableButtons(self):
        for i in range(len(self.buttonArray)):
            for j in range(len(self.buttonArray[i])):
                self.buttonArray[i][j].configure(state = DISABLED)

    def buttonsClicked(self, i, j):
        count = 0
        print(count)
        if(self.gameOver == 0):
            if(self.buttonArray[i][j]["text"] == "X"):
                self.buttonArray[i][j].configure(fg = 'black', bg = 'white')
                self.gameOver = 2 #2 is loss by bomb
            elif(self.buttonArray[i][j]["text"] == " "):
                self.bombCheck(i,j)
            else:
                self.buttonArray[i][j].configure(fg = 'black', bg = 'white', state = DISABLED)
            if(self.gameOver == 0):
                for i in range(len(self.buttonArray)):
                    for j in range(len(self.buttonArray[i])):
                        if(self.buttonArray[i][j]["text"] != "X" and self.buttonArray[i][j]["state"] == "disabled"):
                            count += 1
                            print(count,i,j)
                            if(count == 71):
                                self.gameOver = 1
            if(self.gameOver == 1):
                self.instructionsLabel["text"] = "You win!"
                self.disableButtons()
            elif(self.gameOver == 2):
                self.instructionsLabel["text"] = "Game over, bomb clicked"
                self.disableButtons()


            
        
root = Tk()
root.title("Mine Sweeper")
root.geometry("600x600")

app = Application(root)

root.mainloop()
