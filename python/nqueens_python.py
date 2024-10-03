import numpy as np
def queens(n:int):
    def solve():
        board = np.zeros((n,n),dtype='int64')
        if solve_n_queens_until(board,0) == False:
            print("There are no solutions!!")
            return False
        printqueens(board)
    def solve_n_queens_until(board,col):
        if col >= n:
            return True
        for i in range(n):
            if is_safe(board,i,col):
                board[i][col]=1#place queen and check other places recursively
                if solve_n_queens_until(board,col+1) == True:
                    return True #each queen is placed properly
                board[i][col]=0#each queen is not placed properly remove the queen
        return False
    def is_safe(board,row,col):
        for i in range(col):
            if board[row][i] == 1:
                return False
        for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
            if board[i][j]==1:
                return False
        for i,j in zip(range(row,n,1),range(col,-1,-1)):
            if board[i][j]==1:
                return False
        return True
    def printqueens(board):
        for i in board:
            for j in i:
                if j==0:
                    print(' . ',end='')
                elif j==1:
                    print(" Q ",end='')
            print(" ")
    solve()
queens(11)
    