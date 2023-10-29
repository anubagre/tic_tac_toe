#TicTacToe Game
import numpy as np
board=np.array(['_','_','_','_','_','_','_','_','_'])
print(board.reshape(3,3))
p1s="X"
p2s="O"

def place(sym):
    pos=int(input("Enter position(1-9):"))
    if pos>9 or pos<1:
        print('Invalid input')
    elif (board[pos-1]=='_'):
        board[pos-1]=sym
        print(board.reshape(3,3))
    else:
        print('Position already filled')
        place(sym)
    
def check_rows(sym):
    if(board[0]==board[1]==board[2]==sym):
        print(sym,'Won!')
        return True
    elif(board[3]==board[4]==board[5]==sym):
        print(sym,'Won!')
        return True
    elif(board[6]==board[7]==board[8]==sym):
        print(sym,'Won!')
        return True
    else:
        return False


def check_column(sym):
    if(board[0]==board[3]==board[6]==sym):
        return True
    elif(board[1]==board[4]==board[7]==sym):
        return True
    elif(board[2]==board[5]==board[8]==sym):
        return True
    else:
        return False

def check_diagonal(sym):
    if(board[0]==board[4]==board[8]==sym):
        return True
    elif(board[2]==board[4]==board[6]==sym):
        return True
    else:
        return False   

def won(symbol):
    return check_rows(symbol) or check_column(symbol) or check_diagonal(symbol)


def play():
    for turn in range(9):
        if turn%2==0:
            print('\nTurn of',p1s)
            place(p1s)
            if won(p1s):
                print(p1s,'Won!')
                break
        else:
            print('\nTurn of',p2s)
            place(p2s)
            if won(p2s):
                print(p2s,'Won!')
                break
    if not(won(p1s)) and not(won(p2s)):
        print("Draw")
    
play()
