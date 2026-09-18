class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        total=sum(nums)
        left_sum=0
        for i,v in enumerate(nums):
            right_sum= total-left_sum-v
            if left_sum==right_sum:
                return i 
            left_sum+=v
        return -1
        