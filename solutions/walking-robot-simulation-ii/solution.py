# Problem: Walking Robot Simulation II
# URL: https://leetcode.com/problems/walking-robot-simulation-ii/
# Language: python3

class Robot:

    def __init__(self, width: int, height: int):
        self.w=width
        self.h=height
        self.steps=0
        self.perimeter = 2 * (width + height - 2)
        self.total=0
    def step(self, num: int) -> None:
        self.total+=num
        if self.perimeter>0:
            self.steps=(self.steps+num)% self.perimeter

    def getPos(self) -> List[int]:
        if self.steps==0:
            return [0, 0]
        d = self.steps
        w, h = self.w, self.h
        
        if d<=w-1:
            return [d,0]
        
        d= d - (w-1)
        if d<=h-1:
            return [w-1,d]

        d= d - (h-1)
        if d<=w-1:
            return [(w-1)-d,h-1]

        d= d - (w-1)
        if d<=h-1:
            return [0,(h-1)-d]

    def getDir(self) -> str:
        if self.steps == 0:
            return "East" if self.total==0 else "South"

        d = self.steps
        w, h = self.w, self.h
        
        if d<=w-1:
            return "East"
        
        d-= (w-1)
        if d<=h-1:
            return "North"

        d-= (h-1)
        if d<=w-1:
            return "West"
        return "South"
# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()