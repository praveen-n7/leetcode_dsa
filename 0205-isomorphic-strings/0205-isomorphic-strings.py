class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #understand the isomerphic logic one element is mapped with one element only uniquely 
        if len(s)!= len(t): # if len not equal false 
            return False 
        s_to_t,t_to_s ={},{} #create empty hash maps 
        for a, b in zip(s,t): #iterate through both loops
            if a in s_to_t and s_to_t[a]!=b: return False #check for a in first hash and check if that element is mapped to any other element in b 
            if b in t_to_s and t_to_s[b]!=a: return False #same for b also checking in map of other
            s_to_t[a]=b; t_to_s[b]=a #if not found map them newly and store it in respective maps 
        return True #if the logic suits till the end of the loop return true ie. isomorphic
        