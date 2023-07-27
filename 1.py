import pyfiglet
import random
from colorama import Fore
import time

def show () :
    for line in game_bord :
        for cell in line :
            if cell == "X":
                print ( Fore.RED, cell, Fore.RESET, end = "" )
            
            elif cell == "O" :
                print ( Fore.BLUE, cell, Fore.RESET, end = "" )

            else :
                print ( cell, end = " " )
        print ()
    
def statment () :
    for i in range ( 3 ) :
        if game_bord[i][0] == game_bord[i][1] == game_bord[i][2] == "X" or game_bord[i][0] == game_bord[i][1] == game_bord[i][2] == "O" :
            return ("win")
        
        elif game_bord[0][i] == game_bord[1][i] == game_bord[2][i] == "X" or game_bord[0][i] == game_bord[1][i] == game_bord[2][i] == "O" :
            return ("win")
        
        elif game_bord[0][0] == game_bord[1][1] == game_bord [2][2] == "X" or game_bord[0][0] == game_bord[1][1] == game_bord[2][2] == "O" :
            return ("win")
        
        elif game_bord[0][2] == game_bord[1][1] == game_bord[2][0] == "X" or game_bord[0][2] == game_bord[1][1] == game_bord[2][0] == "O" :
            return ("win")

    t = 0 
    for row in range ( 3 ) :
        for column in range ( 3 ) :
            if game_bord[row][column] != "-" :
                t += 1
    
    if t == 9 :
        return ("equal")
    
    else :
        return ("nothing")

def sec_to_min ( sec ) :
    if sec < 60 :
        min = 0
        return min, sec
    
    elif sec >= 60 :
        min = int ( sec / 60)
        sec = sec - ( min * 60)
        return min, sec

title = pyfiglet.figlet_format ( " Tic Tac Toe ", font = "slant" )
print ( title )
print (" Please enter two numbers between 1 to 3 too show which place do you want to choose to put your taw ")

type = input (" How do you want to play ? enter 'solo' or 'two players' : ")

n = 0
game_bord = [ [ "-", "-", "-"],
              [ "-", "-", "-"],
              [ "-", "-", "-"] ]

show ()
start = time.time ()

if type == "two players" :

    while True :

        row = int ( input (" Please enter the number of the row that you choose : "))
        col = int ( input (" Please enter the number of the column that you choose : "))
    
        if 1 <= row <= 3 and 1 <= col <= 3 :
            if n == 0 :                                                # player 1
                if game_bord [ row - 1 ][ col - 1 ] == "-" :
                    game_bord [ row - 1 ][ col - 1 ] = "X"
                    show ()
                    mood = statment ()
                    if mood == "win" :
                        print (" 🎉 Player 1 Win 🎉 ")
                        break
                    
                    elif mood == "equal" :
                        print (" 🤔 EQUAL 🤔 ")
                        break

                    n = 1
                
                else :
                    print (" 😈😈 Don't cheat 😈😈 ")
                    print (" This place have been chosen ")

            elif n == 1 :                                              # player 2
                if game_bord [ row - 1 ][ col - 1 ] == "-" :
                    game_bord [ row - 1 ][ col - 1 ] = "O"
                    show ()
                    mood = statment ()
                    if mood == "win" :
                        print (" 🎉 Player 2 Win 🎉 ")
                        break
                    
                    elif mood == "equal" :
                        print (" 🤔 EQUAL 🤔 ")
                        break
                    n = 0
                
                else :
                    print (" 😈😈 Don't cheat 😈😈 ")
                    print (" This place have been chosen ")

        
        else :
            print (" 🚫🚫 This place doesn't exist 🚫🚫 ")
    
    end = time.time ()
    min, sec = sec_to_min ( end - start )
    print (Fore.MAGENTA, " This game last ", min, "minute(s) and ", sec, "second(s)"  , Fore.RESET)


elif type == "solo" :

    while True :

        if n == 0 :                                               # player

            row = int ( input (" Please enter the number of the row that you choose : "))
            col = int ( input (" Please enter the number of the column that you choose : "))
            if 1 <= row <= 3 and 1 <= col <= 3 :
                if game_bord [ row - 1 ][ col - 1 ] == "-" :
                    game_bord [ row - 1 ][ col - 1 ] = "X"
                    show ()
                    mood = statment ()
                    if mood == "win" :
                        print (" 🎉 Player Wins 🎉 ")
                        break

                    elif mood == "equal" :
                        print (" 🤔 EQUAL 🤔 ")
                        break

                    print ("________________")
                    n = 1

                else :
                    print (" 😈😈 Don't cheat 😈😈 ")
                    print (" This place have been chosen ")

            else :
                print (" 🚫🚫 This place doesn't exist 🚫🚫 ")

        elif n == 1 :                                             # computer

            row = random.randint ( 0 , 2 )
            col = random.randint ( 0 , 2 )

            if game_bord [ row ][ col ] == "-" :
                game_bord [ row ][ col ] = "O"
                show ()
                mood = statment ()
                if mood == "win" :
                    print (" 🎉 Computer Wins 🎉 ")
                    print (" 😎 YOU LOOS 😎 ")
                    break
                
                elif mood == "equal" :
                    print (" 🤔 EQUAL 🤔 ")
                    break

                n = 0
                
    end = time.time ()
    min, sec = sec_to_min ( end - start )
    print (Fore.MAGENTA, " This game last ", min, "minute(s) and ", sec, "second(s)"  , Fore.RESET)