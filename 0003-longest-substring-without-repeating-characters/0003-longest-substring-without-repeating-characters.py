class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       # l=r=0
        lap={}
        length=l=0
        #last={}
        for r,c in enumerate(s):#check what is enumarate and what is hash
            if c in lap and lap[c]>=l:
                l= lap[c]+1#shrink window by +1 pos if duplicate char found 
            lap[c]=r #storing last  index , value is a index keeper
            length=max(length,r-l+1)
        return length
            
            

        