class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            if token not in '+-*/':  #check for the signs in the stack 
                stack.append(int(token)) #convert it into int as its maths operaton problem and elements are string 
            else:
                b,a=stack.pop(),stack.pop()
                if token == '+':
                    #total+=a+b wrong logic because leads to empty stack pop and mis calculation
                    stack.append(a+b)# the answer must be pushed as an element for further calculation
                elif token =='-':
                    stack.append(a-b)
                elif token == '*':
                    stack.append( a*b)
                else:
                    stack.append (int (a/b))
        return stack.pop() #last element in the stack is the answer

        #NOTE JUST observe the testcases the pattern and get the intution dont think too much as test cases are designed according to a specific pattern,so focus on that pattern and read the question instaruction carefully 

        