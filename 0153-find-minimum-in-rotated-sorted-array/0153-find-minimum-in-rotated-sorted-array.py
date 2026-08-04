class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high = len(nums)-1
        while(low<high):

            mid=(low+high)//2
            if nums[mid]<=nums[high]:#edge case handling 
              
                 high=mid
            else:
                  #left=mid+1 wrong naming
                  low=mid+1#be careful with naming 
               
        return nums[low]#low of the lower side 

        
        