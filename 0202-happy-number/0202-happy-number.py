class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n !=1 and n not in seen: #check for n not 1 and n not seen that is new elements not the repatedd ones
            seen.add(n)
            n=sum(int(d)**2 for d in str(n))#sum the squares convert the int input to string type for easy computaion
        return n==1 #returns true
        #the one with ni ending of sum ends up in infinie loop and returns false 
        