## Program by Julian Borbeck
#01.04.2021

import math
run = True
newgame = True

# config
boardsize = 3 #set size of board, can be larger than classical 3x3 tic tac toe

maxturns = math.floor((boardsize*boardsize)/2)

movedepth = (boardsize*boardsize)
#main loop



#score

def score(board):
    over = False
    winning = 0


    for i in range(0, len(board)):
        row = board[i]

        if (all(element == row[0] for element in row) and row[0] != 0):
            over = True
            winning = row[0]
            return (over, winning)

        column = [board[c][i] for c in range(0, len(board))]
        if (all(element == column[0] for element in column) and column[0] != 0):
            over = True
            winning = column[0]
            return (over, winning)

    # iterate diagonals and check win conditions
    diagonal1 = [board[d1][d1] for d1 in range(0,len(board))]
    diagonal2 = [board[d2][len(board)-d2-1] for d2 in range(0,len(board))]


    if(all(element == diagonal1[0] for element in diagonal1) and diagonal1[0] != 0 ):
        over = True
        winning = diagonal1[0]
        return (over, winning)
    if (all(element == diagonal2[0] for element in diagonal2) and diagonal2[0] != 0):
        over = True
        winning = diagonal2[0]
        return (over, winning)
    return(False,0)

#minimax algorithm

def minimax(board,depth,player):
    #calculate score
    gameover ,winning = score(board)
    #print(depth)
    bestmove  = [-1,-1]
    #initialize best values 
    if(player ==1 ):
        best = -10000000
    if( player == 2):
        best = 10000000
    # set score by depth (solutions that need less moves for the win are better)
    if(gameover == True or depth == 0):
        if(winning == 1):
            scor = -depth
        if(winning == 2):
            scor = depth
        else:
            #draw
            scor = 0

        return scor, [-1,-1]
    else:
            # iterate board, recursively calculate scores and compare them for each level
            for j in range(0, len(board)):

                for k in range(0,len(board)):

                    if (board[j][k] == 0):
                        board[j][k] = player
                        if (player == 1):
                            player = 2
                        else:
                            player = 1
                        res = minimax(board, depth - 1, player)

                        sco = res[0]
                        gameover, winning = score(board)

                        board[j][k] = 0
                        if(player == 1):
                            if (sco > best):
                                best = sco
                                bestmove = [j,k]


                        if(player ==2):
                            if (sco < best):
                                best = sco
                                bestmove = [j,k]

            #return best score and move of level
            return best, bestmove

def renderBoard(board): # draw the board anc check for win conditions

    displaystring = "" # initiate string for printing of board
    over = False # over check flag
    winning = 0
    heading = [x for x in range(0, len(board[0]))] # generate display heading with coordinates
    heading = "".join(str(a) + "\t" for a in heading)
    displaystring += "\t"+heading + "\n"


    # iterate board
    for i in range(0,len(board)):
        row = board[i]

        displaystring += str(i)+"\t"


        #iterate cells and render them as string
        for j in range(0,len(row)):

            # iterate rows for checking and rendering

            cell = row[j]

            if(cell==0):
                displaystring += "▇"
            elif(cell==1):
                displaystring += "X"
            elif(cell==2):
                displaystring += "O"
            if(j<len(row)-1):
                displaystring += "\t"
            else:
                displaystring += "\n"








    print(displaystring)


# set board and check for valid input
def setboard(x,y,player,board):

    if (x.isdigit() and y.isdigit()):
        x = int(x)
        y = int(y)
        if (x <= boardsize-1 and y <= boardsize-1 and x>= 0 and y>= 0):

            if(board[x][y] ==0 ):
                board[x][y] = player
                return True
            else:
                print("this field is already occupied")
                return False
        else:
            print("You need to enter valid coordinates")
            return False
    else:
        print("You need to enter numbers as coordinates")
        return False

# general game calculation and main loop
def game(boardsize,Ai):
    board = [[0] * boardsize for i in range(boardsize)] # create board of size n filled with 0 to indicate it is unoccupied

    turn = 0 # turn counter
    gameover = False # gameover flag to return to games loop

    renderBoard(board) # draw board once at the start

    #main loop
    while(gameover == False):

        turn += 1
        if(turn> maxturns):
            gameover = True
            print("Game over! Its a stalemate!")
            break
        print("Turn: "+str(turn))

        #get inputs
        if(Ai == 1):
            successful = False
            while(successful == False):
                player1 = input("Player X enter move coordinates seperated by comma: ")
                player1 = player1.split(",")
                x = player1[0]
                y = player1[1]
                successful = setboard(x,y,1,board)
            sco, move = minimax(board,movedepth-turn-1,Ai+1)
            print(sco,move)

            if(move[0] != -1 and move[1]!=-1):
                board[move[0]][move[1]] = 2
            renderBoard(board)


        else:
            successful = False

            sco, move = minimax(board, movedepth - turn , Ai + 1)
            print(sco,move)

            if (move[0] != -1 and move[1] != -1):
                board[move[0]][move[1]] = 1
            renderBoard(board)
            while (successful == False):
                player2 = input("Player O enter move coordinates seperated by comma: ")
                player2 = player2.split(",")
                x = player2[0]
                y = player2[1]
                successful = setboard(x, y, 2,board)

        # draw board
        over, winner = score(board)
        renderBoard(board)
        gameover = over

        # check for gameover
        if(winner == 1):
            winner = "X"
        if(winner == 2):
            winner = "O"
        if(gameover == True):
            print("Game over! "+ str(winner)+" wins!")


# games loop to play multiple games
while run == True:

    # initiate game
    valid = False
    while valid == False:
        continueq = input("Play as X or O?")
        if (continueq == "X" or continueq =="O"):
            valid = True
            if(continueq =="X"):
                AI = 1
            else:
                AI = 0

        else:
            valid = False
            print("Please choose a valid answer.")
    game(boardsize,AI)

    # user input + check
    valid = False
    while valid == False:
        continueq = input("Play another game? y/n")
        if(continueq == "y"):
                run = True
                valid = True
        elif(continueq =="n"):
                run = False
                valid = True
        else:
                valid = False
                print("Please choose a valid answer.")
