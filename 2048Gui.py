# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 15:04:03 2021

@author: MadGod
"""


# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 20:02:30 2020

@author: MadGod
"""

# 2048 GAME
import random
import msvcrt
from tkinter import *




def showButtons():     
    global buttons
    buttons = LabelFrame(root, text = "Buttons", font = ("Courier 7 bold"))

    
    upbutton = Button(buttons, text= "Up", fg= "Red", bg="Yellow", command =lambda: Valid(maze,"w"))
    downbutton = Button(buttons, text= "Down", fg= "Red", bg="Yellow", command =lambda: Valid(maze,"s"))
    leftbutton = Button(buttons, text= "Left", fg= "Red", bg="Yellow", command =lambda: Valid(maze,"a"))
    rightbutton = Button(buttons, text= "Right", fg= "Red", bg="Yellow", command =lambda: Valid(maze,"d"))
    
        
    upbutton.grid(row = 9, column= 1, padx= 30, pady = 10)
    downbutton.grid(row = 10, column= 1, pady = 10)
    leftbutton.grid(row = 10, column= 0)
    rightbutton.grid(row = 10, column= 3)
    
    buttons.grid(row = 10, column = 0, columnspan = 5)

        


        

def clear():
    mazeFrame.grid_forget()
    buttons.grid_forget()
    maze[0][0]+=1

def show():
    showButtons()
    PrintMaze(maze)


def getColor(x):
    if x==0:
        return "White"
    elif x==2:
        return "Yellow"
    elif x==4:
        return "Green"
    elif x==8:
        return "Blue"
    elif x==16:
        return "Purple"
    elif x==32:
        return "Orange"
    elif x==64:
        return "Red"
    elif x==128:
        return "Brown"
    elif x==256:
        return "Grey"
    else:
        return "Gold"
    






def PrintMaze(maze):
    global mazeFrame
    mazeFrame = LabelFrame(root, text = "Maze",bd = 2, relief = SUNKEN, font = ("Courier 14 bold"))

    labelList = []
    for i in range(4):
        for j in range(4):
            label = Label(mazeFrame, text = str(maze[i][j]),bg = getColor(maze[i][j]), font = ("Courier 14 bold"),bd = 2, relief = SUNKEN,  padx= 25,
	                pady = 20)
            labelList.append(label)
    print(labelList)   
    z = 0    
    for i in range(4):
        for j in range(4):
            labelList[z].grid(row = i, column = j)    
            z +=1
    mazeFrame.grid(row = 1, column = 0)









# assign new value to a blank place
def NewVal(maze):
    unoc = []
    oc = []
    for i in range(4):
        for j in range(4):
            if maze[i][j] == 0:
                unoc.append([i,j])
            else:
                oc.append([i,j])
    if len(unoc) == 0:
        return True
    x,y = unoc[random.randint(0,len(unoc)-1)]
    maze[x][y] = 2*random.randint(1,2)
    return False


'''            
#Print the maze
def PrintMaze(maze):
    print("\n"*10)
    for i in range(4):
        for j in range(4):
            print("{0: ^6}".format(maze[i][j]), end =" ")
        print("\n\n")
'''


# Moving Elements of a row
def zeroahead(lst):
    x = 0
    for i in range(len(lst)):
        if lst[i] == 0:
            x+=1
        else:
            if x > 0:
                return 1
    return 0     



def ShiftLeft(lst):
    while zeroahead(lst):
        l = []
        for i in range(len(lst)):
            if lst[i] != 0:
                l.append(lst[i])
                lst[i] = 0
        for i in range(len(l)):
            lst[i] = l[i]
    MatchVals(lst)
    while zeroahead(lst):
        l = []
        for i in range(len(lst)):
            if lst[i] != 0:
                l.append(lst[i])
                lst[i] = 0
        for i in range(len(l)):
            lst[i] = l[i]
      

    
def MatchVals(lst):
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            lst[i] *= 2
            global score
            score += lst[i]
            lst[i+1] = 0

           
        
# for moving left
def MoveLeft(maze):
    for j in range(4):
        lst = []
        for i in range(4):
            lst.append(maze[j][i])
        ShiftLeft(lst)
        for i in range(4):
            maze[j][i] = lst[i]
            

def MoveUp(maze):
    for j in range(4):
        lst = []
        for i in range(4):
            lst.append(maze[i][j])
        ShiftLeft(lst)
        for i in range(4):
            maze[i][j] = lst[i]
            

def MoveRight(maze):
    for j in range(4):
        lst = []
        for i in range(4):
            lst.append(maze[j][3-i])
        ShiftLeft(lst)
        for i in range(4):
            maze[j][3-i] = lst[i]
            

def MoveDown(maze):
    for j in range(4):
        lst = []
        for i in range(4):
            lst.append(maze[3-i][j])
        ShiftLeft(lst)
        for i in range(4):
            maze[3-i][j] = lst[i]
        
        
def Move(maze,c):
    
    if c=="a":
        MoveLeft(maze)
    elif c=="d":
        MoveRight(maze)
    elif c=="s":
        MoveDown(maze)
    elif c=="w":
        MoveUp(maze)
    else:
        print("Wrong Move!!!\n")
 
  
    
# check move validity by comparing equality of previous and moved mazes 
def ValidOld(maze,c):    
    m1 = [[0 for i in range(4)  ] for j in range(4)]
    for i in range(4):
        for j in range(4):
            m1[i][j] = maze[i][j]
    m2 = maze
    Move(m2,c)
    for i in range(4):
        for j in range(4):
            if m1[i][j] != m2[i][j]:
                return True
    return False
                 
    


def Valid(maze, c):
    if ValidOld(maze,c):
        NewVal(maze)
        PrintMaze(maze)
    else:
        HIde()







# Game Over by checking validity and 
def GameOver(maze):
    unoc = []
    oc = []
    m = []
    x = 0
    for i in range(4):
        for j in range(4):
            if maze[i][j] == 0:
                unoc.append([i,j])
            else:
                oc.append([i,j])
    if len(unoc) == 0:
        if Valid(maze,"a") or Valid(maze,"d") or Valid(maze,"w") or Valid(maze,"s"):
            pass
        else:
            return False
    return True
    
    

    
'''
one issue: The score is not being stored yet 

# main
k=0
score = 0
maze = [[0 for i in range(4)  ] for j in range(4)]
NewVal(maze)
i = 0

while GameOver(maze):
        PrintMaze(maze) 
        print("Score :",score)
        c = input("Enter the move(wasd)")
        if Valid(maze,c):
            NewVal(maze)
        else:
            print("Invalid Move, Try Again.")
PrintMaze(maze)
print("\n\nGame Over!!!") 

'''



k=0
score = 0
maze = [[0 for i in range(4)  ] for j in range(4)]
NewVal(maze)
i = 0











root = Tk()
Title = Label(root, text = "2048", font = ("Courier 34 bold"), relief = SUNKEN,  padx= 20, pady = 1)
Title.grid(row = 0, column= 0, columnspan = 2)
i =0

PrintMaze(maze)


showButtons()

tbutton = Button(root, text= "HIde", fg= "Red", bg="Yellow", command =clear)     
#tbutton.grid(row = 9, column= 1, padx= 30, pady = 10)
    
tbutton = Button(root, text= "Showde", fg= "Red", bg="Yellow", command =show)     
#tbutton.grid(row = 9, column= 2, padx= 30, pady = 10)    


#root.update()
root.mainloop()
