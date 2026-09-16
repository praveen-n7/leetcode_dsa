class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for x in range(left,right+1):
            if not any(a<=x<=b for a,b in ranges):
                return False
        return True
        