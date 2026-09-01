class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        out=''
        while columnNumber>0:
            columnNumber-=1 #first char starts from zero that is A 
            out = chr(65+columnNumber%26)+out #add the corresponding char to empty string out only the capital char added thats why numbers after 65 
            columnNumber//=26 #update columnnumber to terminate the loop and also process whole number 
        return out
        