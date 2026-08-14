class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i=len(s)-1 #traverse from end 
        while i>=0 and s[i]== ' ': #if space char found move i pointer to the character
            #length=0 #wrong declaration its out of scope 
            i-=1
        length=0 #set the length
        while i>=0 and s[i]!= ' ':# dont forget the s[i] index to be mentioned not just s
            length += 1 #increase length
            i-=1
        return length 
        #obseerve how theb logic of the condition and seqence of the loop and imp variables are wriiten for line by line execution of code to meet final required answer
        