# Problem: Open the Lock
# URL: https://leetcode.com/problems/open-the-lock/
# Language: python3

from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1
        q = deque(["0000"])
        steps = 0
        visited = {"0000"}
        while q:
            for _ in range(len(q)):
                current = q.popleft()
                if current == target:
                    return steps
                for i in range(4):
                    digit = int(current[i])
                    new_digit = (digit+1) % 10
                    new_state = current[:i] + str(new_digit) + current[i+1:]
                    if new_state not in visited and new_state not in dead:
                        q.append(new_state)
                        visited.add(new_state)

                    new_digit = (digit-1 + 10) % 10
                    new_state =  current[:i] + str(new_digit) + current[i+1:]
                    if new_state not in visited and new_state not in dead:
                        q.append(new_state)
                        visited.add(new_state)
            steps+=1
        return -1