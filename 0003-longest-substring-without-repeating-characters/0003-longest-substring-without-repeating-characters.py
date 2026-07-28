class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       # l=r=0
        last={}
        length=l=0
        last={}
        for r,c in enumerate(s):#check what is enumarate and what is hash
            if c in last and last[c]>=l:
                l= last[c]+1#shrink window by +1 pos if duplicate char found 
            last[c]=r
            length=max(length,r-l+1)
        return length
            
            

        