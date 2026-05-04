class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        #check if 3by3 is valid
        for i in range(0,n,3):
            currY = 0
            while currY < n:
                seen = [-1 for i in range(10)]
                for j in range(currY,currY+3):
                    pos = board[i][j]
                    if pos == ".":
                        pass
                    elif seen[int(pos)] != -1:
                        return False
                    else:
                        seen[int(pos)] = 1
                    #pos2
                    pos2 = board[i+1][j]
                    if pos2 == ".":
                        pass
                    elif seen[int(pos2)] != -1:
                        return False
                    else:
                        seen[int(pos2)] = 1
                    #pos3
                    pos3 = board[i+2][j]
                    if pos3 == ".":
                        pass
                    elif seen[int(pos3)] != -1:
                        return False
                    else:
                        seen[int(pos3)] = 1
                currY+=3
        #check if col is valid
        for i in range(n):
            seen = [-1 for i in range(10)]
            for j in range(n):
                pos = board[i][j]
                if pos == ".":
                        pass
                elif seen[int(pos)] != -1:
                    return False
                else:
                    seen[int(pos)] = 1
         #check if row is valid
        for i in range(n):
            seen = [-1 for i in range(10)]
            for j in range(n):
                pos = board[j][i]
                if pos == ".":
                        pass
                elif seen[int(pos)] != -1:
                    return False
                else:
                    seen[int(pos)] = 1
        return True
                
