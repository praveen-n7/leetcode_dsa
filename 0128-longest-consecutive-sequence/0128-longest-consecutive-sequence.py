class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        max_len=0
        for num in num_set:
            if num-1 not in num_set:#checks for preceding num to start only this condition is valid for the start point 
                cur,length = num,1 #sets or resets the parameters for countng
                while cur +1 in num_set: #checks for succeeding num
                    cur+=1;length+=1
                max_len =  max(max_len,length)
        return max_len
        