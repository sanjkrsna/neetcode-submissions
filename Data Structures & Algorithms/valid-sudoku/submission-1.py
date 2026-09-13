class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            seen = set()
            for c in range(9):
                val = board[r][c]
                if val != ".":
                    if val in seen:
                        return False
                    seen.add(val)

        for c in range(9):
            seen = set()
            for r in range(9):
                val = board[r][c]
                if val != ".":
                    if val in seen:
                        return False
                    seen.add(val)


        for r_box in range(0,9,3):
            for c_box in range(0,9,3):
                seen = set()
                for r in range(r_box,r_box+3):
                    for c in range(c_box,c_box+3):
                        val = board[r][c]
                        if val != ".":
                            if val in seen:
                                return False
                            seen.add(val)

        return True 
        

        