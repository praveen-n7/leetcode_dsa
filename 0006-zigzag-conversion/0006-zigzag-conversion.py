class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows ==1 or num_rows >= len(s): return s 
        rows=[[] for _ in range (num_rows)]
        row,direction = 0,-1
        for c in s :
            rows[row].append(c)
            if row ==0 or row == num_rows -1:
                direction = -direction
            row+=direction
        return ''.join(''.join(r) for r in rows)
        