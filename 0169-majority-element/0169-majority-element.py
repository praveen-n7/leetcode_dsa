class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate,count=None,0
        for n in nums:
            if count == 0: #no chance pf negative entering of candidate
                candidate=n
            count+=1 if candidate==n else -1 #one line  if else for count+=1 and count-=1
        return candidate