class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for r in range(9):
            for c in range(9):
                rows = []
                for col in range(9):
                    if board[r][col].isdigit():
                        rows.append(board[r][col])
                cols = []
                for row in range(9):
                    if board[row][c].isdigit():
                        cols.append(board[row][c])
                if len(rows) != len(set(rows)) or len(cols) != len(set(cols)):
                    print("row ",rows)
                    print("column ",cols)
                    return False
                if r < 3: row_cap = 3
                elif r < 6: row_cap = 6
                else : row_cap = 9
                if c < 3: col_cap = 3
                elif c < 6: col_cap = 6
                else : col_cap = 9
                sub_mat = []
                for sub_r in range(row_cap-3,row_cap):
                    for sub_c in range(col_cap-3,col_cap):
                        if board[sub_r][sub_c].isdigit():
                            sub_mat.append(board[sub_r][sub_c])
                if len(sub_mat) != len(set(sub_mat)): 
                    print("sub_mat " , sub_mat)
                    return False
        return True
