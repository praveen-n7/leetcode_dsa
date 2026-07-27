class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        l=count=0
        n=len(nums)
        while l<n:
            if nums[l]%2!=0 or nums[l]>threshold : #imp line from given condition
                l+=1
                continue  #continues the loop doesnt go to next line
            r=l
            while r+1<n and nums[r+1]<=threshold  and nums[r+1]%2!=nums[r]%2 : #boundary condition are imp understand it
                r+=1
            count=max(count,r-l+1)
            l=r+1
        return count

                
        
                

        
    
        