class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate,count=None,0
        for n in nums:
            if count == 0: #no chance pf negative entering of candidate
                candidate=n
            count+=1 if candidate==n else -1 #one line  if else for count+=1 and count-=1
        return candidate
        #NOTE this algo is used with condition of majority element appearing greatter than n/2 times so the count + and - works correctly to get the desired output 