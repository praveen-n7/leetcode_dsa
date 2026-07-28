class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length=float('inf')
        left=0
        window_sum=0
        for right in range(len(nums)):
             #index is imp thatsb why used range and not nums
             window_sum+=nums[right]
             while(window_sum>=target):#use of while not if , to adjust and come out of this block to  expand from right side 
                length=min(length,right-left+1)
                window_sum-=nums[left]
                left+=1
                
        return 0 if length==float('inf') else length

            
                
             
                          
                
            
        