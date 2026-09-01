class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        out=''
        while columnNumber>0:
            columnNumber-=1 # modulo operator % works with 0 A 1 B 2 C 
            out = chr(65+columnNumber%26)+out #add the corresponding char to empty string out only the capital char added thats why numbers after 65 
            columnNumber//=26 #update columnnumber to terminate the loop and also process whole number 
        return out
        