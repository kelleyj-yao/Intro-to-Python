import time
import os
import msvcrt
import io
import csv

MAX_ROW = 40  # total number of rows
MAX_COL = 80  #total number of columns

currentGen = [['-' for i in range(0,MAX_ROW)] for j in range(0,MAX_COL)]

tempList = [['-' for i in range(0,MAX_ROW)] for j in range(0,MAX_COL)]

def displayMenu():
    print(" Press [P] to play. \n Press [Q] to exit.")
    print(" Press [U] to load 'U' pattern. \n Press [S] to stop. \n Press [C] to clear the grid. \n Press [M] to enter Manual mode. ")


def setZeroList(list):
    for i in range(MAX_COL-1):
        for j in range(MAX_ROW-1):
            list[i][j]='-'
    return list
    
def setInitialPatternList(tempGen):
    import random
    row_start=random.randint(0,MAX_COL-7)
    col_start=random.randint(0,MAX_ROW-8)
    
    tempGen[row_start][col_start]='X'
    tempGen[row_start][col_start+6]='X'

    for i in range(1,5):
        tempGen[row_start+i][col_start]='X'

    for i in range(1,5):
        tempGen[row_start+i][col_start+6]='X'

    for i in range(0,7):
        tempGen[row_start+5][col_start+i]='X'
  

def copyList(firstList):
        newList=[row[:] for row in firstList]
        return newList

def displayList(anyList):
    for i in anyList:
        print (*i, sep='')

def displaySubMenu():
    print('''[S]top – Press 'S' to stop. ''')

def setNextGenList( inputList ):
    # checking 8 squares around 1st location, using for loop??
    currentGen = copyList( inputList )
    
    for i in range(1,MAX_COL):
        for j in range(1,MAX_ROW):
            try:
                NumberOfNeighbors = 0
                if inputList[(i)+1][j]=='X':
                    NumberOfNeighbors += 1

                if inputList[(i)-1][j]=='X':
                    NumberOfNeighbors += 1

                if inputList[i][(j)+1]=='X':
                    NumberOfNeighbors += 1

                if inputList[i][(j)-1]=='X':
                    NumberOfNeighbors += 1

                if inputList[(i)+1][(j)+1]=='X':
                    NumberOfNeighbors += 1

                if inputList[(i)+1][(j)-1]=='X':
                    NumberOfNeighbors += 1

                if inputList[(i)-1][(j)+1]=='X':
                    NumberOfNeighbors += 1

                if inputList[(i)-1][(j)-1]=='X':
                    NumberOfNeighbors += 1
                
                if inputList[i][j]=='X':
                    if NumberOfNeighbors < 2 or NumberOfNeighbors > 3:
                        currentGen[i][j]='-'  
                        
                if inputList[i][j]=='X':
                    if NumberOfNeighbors==2 or NumberOfNeighbors==3:
                        currentGen[i][j]='X'
                    
                if inputList[i][j]=='-':
                    if NumberOfNeighbors==3:
                        currentGen[i][j]='X'   
                    
            except IndexError:
                NumberOfNeighbors += 0
    return currentGen

def manualMode():
    print ('Input the size of rows and columns, separated by a comma:') 
    manInput=input().split(',')
    MAN_ROW,MAN_COL=manInput[0],manInput[1]
    manList = [['-' for i in range(0,int(MAN_ROW))] for j in range(0,int(MAN_COL))]
    return [manList, MAN_COL, MAN_ROW]

def manualPattern(inputList, MAN_ROW_VAL, MAN_COL_VAL):
    userPat=int(input())
    if userPat==1:
        Football = patternOne(inputList, MAN_ROW_VAL, MAN_COL_VAL)
        displayList( Football )
        return Football
        
    elif userPat==2:
        ShipPat = patternTwo(inputList, MAN_ROW_VAL, MAN_COL_VAL)
        displayList( ShipPat )
        return ShipPat

    else:
        Trampoline = patternThree(inputList, MAN_ROW_VAL, MAN_COL_VAL)
        displayList( Trampoline )
        return Trampoline

def patternOne(list, row, col):
    import random
    row_start=random.randint(0,int(col)-4)
    col_start=random.randint(0,int(row)-4)

    file = open("football.txt", "r" )
    x,y = [], []
    for i in file:
        row = i.split()
        x.append(row[0])
        y.append(row[1])
    
    list[row_start+int(x[0])][col_start+int(y[0])]='X'
    list[row_start+int(x[1])][col_start+int(y[1])]='X'
    list[row_start+int(x[2])][col_start+int(y[2])]='X'
    list[row_start+int(x[3])][col_start+int(y[3])]='X'
    list[row_start+int(x[4])][col_start+int(y[4])]='X'
    list[row_start+int(x[5])][col_start+int(y[5])]='X'

    return list

def patternTwo(list, row, col):
    import random
    row_start=random.randint(0,int(col)-3)
    col_start=random.randint(0,int(row)-3)
    
    file = open("ship.txt", "r" )
    x,y = [], []
    for i in file:
        row = i.split()
        x.append(row[0])
        y.append(row[1])

    list[row_start+int(x[0])][col_start+int(y[0])]='X'
    list[row_start+int(x[1])][col_start+int(y[1])]='X'
    list[row_start+int(x[2])][col_start+int(y[2])]='X'
    list[row_start+int(x[3])][col_start+int(y[3])]='X'
    list[row_start+int(x[4])][col_start+int(y[4])]='X'
    list[row_start+int(x[5])][col_start+int(y[5])]='X'

    return list

def patternThree(list, row, col):
    import random
    row_start=random.randint(0,int(col)-4)
    col_start=random.randint(0,int(row)-4)

    file = open("trampoline.txt", "r" )
    x,y = [], []
    for i in file:
        row = i.split()
        x.append(row[0])
        y.append(row[1])
    
    list[row_start+int(x[0])][col_start+int(y[0])]='X'
    list[row_start+int(x[1])][col_start+int(y[1])]='X'
    list[row_start+int(x[2])][col_start+int(y[2])]='X'
    list[row_start+int(x[3])][col_start+int(y[3])]='X'
    list[row_start+int(x[4])][col_start+int(y[4])]='X'
    list[row_start+int(x[5])][col_start+int(y[5])]='X'

    return list

def saveArray( list ):
    with open(input('Write file name: '), 'w', newline='') as file:
        writer = csv.writer(file, delimiter=' ')
        writer.writerows(list)

    file.close()
    return file

def loadArray( file ):
    with open(input('Write file name: '), 'r') as file:
        for i in file:
            i=i.rstrip()
            print (i.replace(" ",""))
    file.close()


def main():
    displayMenu()
    tempGen=setZeroList(tempList)
    displayList( tempGen )
    askInput=input()
    if askInput=='u' or askInput=='U':
        setInitialPatternList(tempGen)
        currentGen=copyList(tempGen)
        displayList(currentGen)
        userInput=input()
        while userInput=='p' or userInput=='P':
            while not msvcrt.kbhit():
                os.system('cls')
                print('Press [S] to stop.')
                currentGen1=setNextGenList(currentGen)
                displayList(currentGen1)
                currentGen = currentGen1
                time.sleep(2)
            userInput=msvcrt.getch().decode()
            print(userInput)
            if userInput=='s' or userInput=='S':
                os.system('pause')
            elif userInput=='c' or userInput=='C':
                os.system('cls')
                time.sleep(2)
            elif askInput=='q' or askInput=='Q':
                quit()


    elif askInput=='m' or askInput=='M':
        manList, MAN_ROW, MAN_COL = manualMode()
        print("Football - press '1' to load. \nShip - press '2' to load. \nTrampoline - press '3' to load.")
        userGenList = manualPattern(manList, MAN_ROW, MAN_COL)
        print('Press Z to save your current array: ')
        secondInput = input()
        if secondInput=='Z' or secondInput=='z':
            testList = saveArray( userGenList )
            print( 'Press L to load your current array:' )
            thirdInput = input()
            if thirdInput=='L' or thirdInput=='l':
                loadArray(testList)
                os.system('pause')
            else:
                quit()
        else:
            quit()
    else:
        quit()


main()
