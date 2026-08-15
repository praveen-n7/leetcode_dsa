class Solution:
    def romanToInt(self, s: str) -> int:
        table = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}# prepare a hash map of roman char and their vaalues
        total=0
        for i,ch in enumerate(s):#iterate via string 
            cur = table[ch]
            nxt=table[s[i+1]] if i+1 < len(s) else 0#comapre current char and next char with logic of roman numbers
            total+=-cur if cur< nxt else cur
        return total
        