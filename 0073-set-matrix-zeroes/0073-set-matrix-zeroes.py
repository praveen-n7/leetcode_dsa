class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows,cols = set(),set() #two hash for rows and cols data check 
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):#len matrix[0](4) not len matrix(3)
                if matrix[r][c]==0:rows.add(r); cols.add(c) #if zero found stire it in hash 
        for r in range (len(matrix)):
            for c in range(len(matrix[0])):
                if r in rows or c in cols: matrix[r][c]=0 # if hash value is true make those r and c vlaues index values of matrix and make that value zero
        