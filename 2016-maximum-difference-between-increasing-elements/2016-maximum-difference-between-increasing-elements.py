class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        min_so_far=nums[0]
        best=-1
        for i in range(1,len(nums)):
            if nums[i]>min_so_far:
                best=max(best,nums[i]-min_so_far)
            else:
                min_so_far=nums[i]
        return best
        