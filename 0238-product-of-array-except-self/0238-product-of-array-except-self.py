class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L=1 #extra value to provide a missync between the indices
        n=len(nums)
        ans=[0]*n
        for i in range(n):
            ans[i]=L #storing prefix sum in one pass
            L*=nums[i]
        R=1 #to ignore the last index value as in the 1st pass we git the correct value at this index ignoring itself
        for i in range(n-1,-1,-1):#this section is thee logic for skipping the index value of its own for product calculation and the calculated product is stired in the current index witjout considering its own value 
            ans[i]*=R 
            R*=nums[i]
        return ans
        #tricky problem 
        