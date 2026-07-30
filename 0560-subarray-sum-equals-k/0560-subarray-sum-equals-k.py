class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq={0:1} #to count value itself if its value is present as whole vlaue in array the second test case handle 
        count = pre=0
        for i in range(len(nums)):
            pre+=nums[i]
            need = pre - k #in prefix sum the need is beside the pre oly if it exist 
            if need in freq:
                count+=freq[need] #finds need value as key pair and increments count by adding its value 
            freq[pre]=freq.get(pre,0)+1# hash map stores values as key and count as value  
        return count 
#tricky sum too 