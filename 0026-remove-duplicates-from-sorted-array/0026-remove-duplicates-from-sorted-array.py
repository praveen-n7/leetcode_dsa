class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0 #edge case handle is imp
        nums.sort()
        f=0
        for j in range(f+1,len(nums)):
            if(nums[f]!=nums[j]):
                
                f+=1
                nums[f]=nums[j]
            continue
        return f+1
        