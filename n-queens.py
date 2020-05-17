
#checking if the list "partial" represents a legal board
def legal(partial, i):
    n = len(partial)
    Queen_dict = {}
    for row in partial:
        if 'Q' in row:
            if row.index('Q') == i:
                return False
            Queen_dict[partial.index(row)] = row.index('Q')
        else:
            j = partial.index(row)
            break #found the empty line
    for key in Queen_dict.keys():
        if abs(key - j) == abs(Queen_dict[key] - i): #checking diagonal line
            return False
    return True

#recursive function: checking number of legal boards size nxn
def queens(n):
    loc_lst = []
    if n == 2 or n == 3: #no options for legal board
        return 0
    if n == 0 or n == 1: #the empty selection of legal board
        return 1
    return rec_queens(n,loc_lst)

def rec_queens(n,loc_lst):
    if len(loc_lst) == n:
        return 1 #option found
    cntOption = 0
    for i in range(n):
        if legal_list(loc_lst,i,n):
            cntOption += rec_queens(n, loc_lst + [i])
    return cntOption


def legal_list(lst,i,n):
    '''the function uses the function legal
    on a list instead of on a board'''
    board = [[' ' for x in range(n)] for y in range (n)]
    for j in range(len(lst)):
            board[j][lst[j]] = 'Q'
    return legal(board,i)


#Boolean: returns if it is legal to locate queen in board[row][col]
def legal_dragons(board,row,col):
    n = len(board)
    if len(board) == 0:
        return True
    if board[row][col] == 'D':
        return False
    
    for i in range(col-1,-1,-1): #left
        if board[row][i] == 'D':
            break
        if board[row][i] == 'Q':
            return False
        
    for i in range(row-1,-1,-1): #up
        if board[i][col] == 'D':
            break
        if board[i][col] == 'Q':
            return False
        
    j, i = row-1, col-1
    while i >= 0 and j >= 0: #Diagonal
        if board[j][i] == 'D':
             break
        if board[j][i] == 'Q':
            return False
        j -= 1
        i -= 1
        
    j,i = row+1,col-1
    while i >= 0 and j < n: #Diagonal
        if board[j][i] == 'D':
             break
        if board[j][i] == 'Q':
            return False
        j += 1
        i -= 1
        
    return True
    

    
def queens_dragons(board):
    return queens_dragons_rec(len(board), 0, 0, board)



#counting the number of legal options to locate n queen in board
def queens_dragons_rec(remaining, row, col, board):
    n = len(board)
    cntOption  = 0
    if remaining == 0:
        return 1
    if col == n:
        return 0
    if row == n:
        cntOption  +=  queens_dragons_rec(remaining, 0, col+1, board)
    else:
        if legal_dragons(board,row,col):
            board[row][col] = 'Q'
            cntOption  +=  queens_dragons_rec(remaining-1, row+1, col, board)
            board[row][col] = ' '
        cntOption  +=  queens_dragons_rec(remaining, row+1, col, board)
    return cntOption

