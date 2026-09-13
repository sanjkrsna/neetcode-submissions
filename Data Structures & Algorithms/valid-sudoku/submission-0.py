class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = defaultdict(set)
        col_hash = defaultdict(set)
        square_hash = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                elif board[r][c] in row_hash[r]:
                    return False
                elif board[r][c] in col_hash[c]:
                    return False
                elif  board[r][c] in square_hash[(r//3,c//3)]:
                    return False
                row_hash[r].add(board[r][c])
                col_hash[c].add(board[r][c])
                square_hash[(r//3,c//3)].add(board[r][c])
        return True
                

        