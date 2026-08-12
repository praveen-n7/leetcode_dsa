class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result =[]
        for i in range (numRows):
            row=[1]*(i+1)#edge ones  condition
            for j in range(1,i):#index after onw entry of one near edges
                row[j]=result[i-1][j-1]+result[i-1][j]#boundary control logic 
            result.append(row)#append after every j loop completion
        return result
        