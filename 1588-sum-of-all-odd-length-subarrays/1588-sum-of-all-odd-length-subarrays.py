class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        total = 0
        n=len(arr)
        for i in range(n):
            L=1
            while i+L<=n:
                s=sum(arr[i:i+L])
                total+=s
                L+=2
        return total
        