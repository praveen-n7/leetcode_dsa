class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):#the range of the loop start is end of array and end is -1 that is beyond index 0 because to add 1 at beginning in case of 9 digit
            if digits[i]<9:
                digits[i]+=1
                return digits
            digits[i]=0
        return [1]+digits #adds 1 at te index 0 while shifting rest of te digits t the right 
        