class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write=0
        for x in nums:
            if (write<2 or x!=nums[write-2]): #edge is also handeled in this condition
                nums[write]=x
                write+=1 #alraedy get 2 ++ for the 1st if condition udnerstand every piece of code 
        return write
        