class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={} #freq counter
        L=max_freq=best=0
        for r,c in enumerate(s):
            count[c] = count.get(c,0)+1
            max_freq=max(max_freq,count[c])
            while(r-L+1-max_freq>k):#check window is valid or not and adjust accordingly
               # count[L]-=1 mistake,L is an index and for count we need char as key to get the value,so L gets the char at that index from a that  string 
               count[s[L]]-=1
               L+=1
            best=max(best,r-L+1)#get the max length of valid window
        return best
        