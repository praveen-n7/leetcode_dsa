class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_max = curr_min=nums[0]
        max_sum=nums[0]
        min_sum=nums[0]
        total_sum=nums[0] #mistake made it zero but our tracking start from index 1 so it get ignored
        for i in range(1,len(nums)):
            curr_min = min(nums[i],curr_min+nums[i])
            min_sum=min(min_sum,curr_min)
            curr_max=max(nums[i],curr_max+nums[i])
            
            max_sum=max(max_sum,curr_max)
            total_sum+=nums[i]
        return max_sum if max_sum<=0 else max(max_sum,total_sum-min_sum) #to handle the cirrcular concept of array and also for also all negative vlaues(1st condition)

