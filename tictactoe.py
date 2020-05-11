"""
Tic Tac Toe Player
"""

import math
import sys

X = "X"
O = "O"
EMPTY = None
turn=1
moves=[]

def initial_state():
    """
    Returns starting state of the board.
    """
    global turn
    turn=1
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    global turn
    if turn==0:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    global EMPTY
    actions=[]
    x=0
    y=0
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                actions.append([i,j])
        
    return actions
    

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    
    i=action[0]
    j=action[1]

    board[i][j]=player(board)
    global turn
    if turn==0:
        turn=1
    elif turn==1:
        turn=0
        
    return board

def undo_action(board, action):
    board[action[0]][action[1]] = None
    global turn
    if turn==0:
        turn=1
    elif turn==1:
        turn=0

    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0]==board[1][1]==board[2][2]==O :
        return O
    
    elif board[0][0]==board[1][1]==board[2][2]==X :
        return X

    
    elif board[2][0]==board[1][1]==board[0][2]==O :
        return O
    
    elif board[2][0]==board[1][1]==board[0][2]==X :
        return X


    elif board[2][0]==board[2][1]==board[2][2]==O :
        return O

    elif board[2][0]==board[2][1]==board[2][2]==X :
        return X


    elif board[1][0]==board[1][1]==board[1][2]==O :
        return O

    elif board[1][0]==board[1][1]==board[1][2]==X :
        return X


    elif board[0][0]==board[0][1]==board[0][2]==O :
        return O
    
    elif board[0][0]==board[0][1]==board[0][2]==X :
        return X

    
    elif board[0][0]==board[1][0]==board[2][0]==O :
        return O
    
    elif board[0][0]==board[1][0]==board[2][0]==X :
        return X

    
    elif board[0][1]==board[1][1]==board[2][1]==O :
        return O

    elif board[0][1]==board[1][1]==board[2][1]==X :
        return X


    elif board[0][2]==board[1][2]==board[2][2]==O :
        return O
    
    elif board[0][2]==board[1][2]==board[2][2]==X :
        return X
    else :
        return

    
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY :
                return False

    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board)==O:
        return -1
    elif winner(board)==X:
        return 1
    else :
        return 0

def best_score(board,depth,is_max):
    """
    Returns the optimal action for the current player on the board.
    """
    
    if winner(board)==X:
        return 10 - depth
    elif winner(board)==O:
        return -10 + depth
    elif terminal(board)==True:
        return 0

    action = actions(board)

    if is_max:
        best = -sys.maxsize

        for act in action:
            val = best_score(result(board, act), depth + 1, False)
            undo_action(board, act)
            best = max(best, val)
    else:
        best = sys.maxsize

        for act in action:
            val = best_score(result(board, act), depth + 1, True)
            undo_action(board, act)
            best = min(best, val)

    return best

def minimax(board):
    p=player(board)
    global turn
    if player(board)==X:
        enemy=O
    else :
        enemy=X
        
    action = actions(board)
    best_i = None
    best_val = -sys.maxsize

    for i, act in enumerate(action):
        val = best_score(result(board, act), 0, False)
        board[act[0]][act[1]] = None

        if val > best_val:
            best_i = i
            best_val = val

    if p==X:
        turn=1
    else :
        turn=0
    return action[best_i]
