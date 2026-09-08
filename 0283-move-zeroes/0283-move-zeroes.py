class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write=0 #note rad and write both are pointers for index managing 
        for read in range(len(nums)):
            if nums[read]!=0:
                nums[write],nums[read]=nums[read],nums[write] #adjusting the readand write value for the desired moment to move zeroes to the end(block movement animations) 
                write+=1
        