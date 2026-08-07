class Solution:
    def isValid(self, s: str) -> bool:
        stack=[] #create a empty stack
        match = {')':'(',']':'[','}':'{'} #create a match for comparison
        for ch in s:
            if ch in "([{": #check if char is one of them 
                stack.append(ch)
            elif not stack or stack.pop()!=match[ch]: #the top after pop and match of current ch must be equal to match 
                return False 
        return not stack #return true if stack empty 