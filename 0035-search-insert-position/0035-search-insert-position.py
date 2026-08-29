class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if(nums[i]>=target): #array is sorted so if equal returns index if greater returns index to be inserted very smart approach of conditional statement for output
                return i
        return len(nums) #if target greater than the greatest element if the element then return len of arr as index to be inserted
        
        

        