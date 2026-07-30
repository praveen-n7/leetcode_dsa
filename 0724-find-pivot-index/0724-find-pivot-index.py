class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum=0
        total=sum(nums)
        for i, v in enumerate(nums):
            if(left_sum==total-left_sum-v):#imp line to handle edge cases and also this logic is return to get the rightsum 
                return i
            left_sum+=v
        return -1
        