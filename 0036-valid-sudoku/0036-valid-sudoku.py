class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        seen =set()  #store the numbs  already seen in each row  column and box

        for r in range(9):  #go through each row
            for c in range(9):  #go through each column in that row

                v = board[r][c]  #get the value from the current cell

                if v == '.':  #if the cell is empty, there is nothing to check
                    continue  # skip this cell and move to the next one

                b = (r // 3) * 3 + (c // 3)  #find which 3x3 box this cell belongs to

                #make unique keys for this number s row column and box
                keys = (
                    f"r{r}{v}",  #represents this number in the current row
                    f"c{c}{v}",  #represents this number in the current column
                    f"b{b}{v}"   #represents this number in the current 3x3 box
                )

                #if any of these keys already exists the number is repeated
                if any(k in seen for k in keys):
                    return False  # repeated number means the Sudoku is invalid

                seen.update(keys)  #remember this number in its row column and box

        return True  #if no duplicates were found, the Sudoku is valid