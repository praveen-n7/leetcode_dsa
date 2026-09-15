class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        best,best_year=0,1950
        for y in range(1950,2051): #range from 1950 stsrt point 2051 end point 
            count = sum(1 for b,d in logs if b<=y<d) #checking of no of person alive condition logic 
            if count > best:
                best = count
                best_year=y
        return best_year #returning best year y from range mentioned above 
        