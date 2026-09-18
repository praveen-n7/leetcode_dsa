class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        n=len(gain)
        altitude =[0]*(n+1)
        for i in range(n):
            altitude[i+1]=altitude[i]+gain[i]
        best = 0
        for v in altitude:
            if v > best:
                best=v
        return best
        