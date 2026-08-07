class MinStack:
#dont forget to mention self because self means considering its own instance as an arguement 
    def __init__(self):
        self.stack=[]
        self.stackMin=[] # to maintain min element at the top to easily return the min element 
        

    def push(self, value: int) -> None:
        self.stack.append(value)
        self.stackMin.append(min(value,self.stackMin[-1]) if self.stackMin else value)# pushing the most min element in the stack if empty stack push the value if not push the minimum elemnet of bith 
        

    def pop(self) -> None:
        self.stackMin.pop() # this is because the element should be popped out of both stack because old min can still be there if its popped out of original stack so in order to overcome this case 
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1] #return top of the stack
        

    def getMin(self) -> int:
        return self.stackMin[-1] #return the top of minstack 
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()