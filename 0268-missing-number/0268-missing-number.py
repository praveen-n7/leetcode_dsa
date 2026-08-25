class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort(); low,high =0,len(nums)#sort first and assign the range values
        while low < high:
            mid=low+(high-low)//2 #mid value updation when high and low values get upfated respevtively accoriding to condition
            if nums[mid]>mid:high =mid
            else : low=mid+1
        return low