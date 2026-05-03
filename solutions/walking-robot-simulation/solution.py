# Problem: Walking Robot Simulation
# URL: https://leetcode.com/problems/walking-robot-simulation/
# Language: python3

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x,y=0,0
        obstacles = set(map(tuple, obstacles))
        # North, East, South, West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = 0
        curr_direction = 0
        for cmd in commands:
            if cmd==-2:
                curr_direction= (curr_direction+3)%4
                continue
            if cmd==-1:
                curr_direction= (curr_direction+1)%4
                continue
            else:
                dx, dy = directions[curr_direction]
                for _ in range(cmd):
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in obstacles:
                        break
                    x, y = nx, ny
                    res = max(res, x**2 + y**2)
        return res
