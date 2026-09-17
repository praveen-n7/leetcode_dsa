class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        n=len(nums)
        result =[0]*n
        for i in range(n):
            s=0
            for j in range(i+1):
                s+=nums[j]
            result[i]=s
        return result
        