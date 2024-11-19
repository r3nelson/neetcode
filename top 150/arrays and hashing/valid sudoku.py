class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # columns can't contain duplicates
        # rows can't contain duplicates
        # 3X3 square can't contain duplicates
        
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == ".":
                    continue

                if (board[r][c] in rows[r]            
                    or board[r][c] in cols[c] 
                    or board[r][c] in squares[(r//3, c//3)]):
                    return False
                
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        
        return True
                