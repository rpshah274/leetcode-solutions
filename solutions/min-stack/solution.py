# Problem: Min Stack
# URL: https://leetcode.com/problems/min-stack/
# Language: python3

class MinStack:

    def __init__(self):
        self.minstack=[] 
        self.stack=[]
       
    def push(self, val: int) -> None:
        self.minstack.append(val)
        if not self.stack or val<=self.stack[-1]:
            self.stack.append(val)

    def pop(self) -> None:
        v=self.minstack.pop()  
        if self.stack and v==self.stack[-1]:
            self.stack.pop() 

    def top(self) -> int:
        return self.minstack[-1]

    def getMin(self) -> int:
        return self.stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()