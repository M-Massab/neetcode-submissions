class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:  
        rows = [None] * 9
        cols = [None] * 9
        boxs = [None] * 9

        for i in range(9):
            rows[i] = set()
            cols[i] = set()
            boxs[i] = set()

        for i in range(9):
            for j in range(9):
                current = board[i][j]
                if current == ".":
                    continue
                
                boxindex = (i // 3) * 3 + (j // 3)  
                
                if current in rows[i] or current in cols[j] or current in boxs[boxindex]:
                    return False
                    
                rows[i].add(current)    
                cols[j].add(current)    
                boxs[boxindex].add(current)    
                
        return True