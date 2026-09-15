class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        best,best_year=0,1950
        for y in range(1950,2051):
            count = sum(1 for b,d in logs if b<=y<d)
            if count > best:
                best = count
                best_year=y
        return best_year
        