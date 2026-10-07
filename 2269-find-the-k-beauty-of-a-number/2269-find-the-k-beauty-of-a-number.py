class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s=str(num)
        count =0 
        for i in range(len(s)-k+1):
            w=int(s[i:i+k])
            if w!=0 and num %  w==0:
                count+=1
        return count #general approach 