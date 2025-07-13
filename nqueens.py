# Check if n queens can be kept in an nxn chessboard

def isAttacking(i, j):
    for l in range(k):
        if chessboard[l][j] == 1 or chessboard[i][l] == 1:
            return True
    for l in range(k):
        for m in range(k):
            if l+m == i+j and chessboard[l][m] == 1:
                return True
            if l-m == i-j and chessboard[l][m] == 1:
                return True 
    return False

def nQueens(n):
    if n == 0:
        return True
    
    for i in range(k):
        for j in range(k):
            if not isAttacking(i,j) and chessboard[i][j] == 0:
                chessboard[i][j] = 1
                if nQueens(n-1):
                    return True
                chessboard[i][j] = 0  
    return False

k = int(input("Enter the number : "))
chessboard = [[0]*k for _ in range(k)]
print(nQueens(k))
