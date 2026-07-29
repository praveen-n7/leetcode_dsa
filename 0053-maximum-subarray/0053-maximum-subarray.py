class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        max_sum=nums[0]
        for i in range(1,len(nums)):#i must start from index 1 because nums[0]already initialized to current
            current = max(nums[i],nums[i]+current) #find max between prev subarray sum and current value to decide whether to contiue or start a new subarray
            max_sum=max(max_sum,current)
        return max_sum
        