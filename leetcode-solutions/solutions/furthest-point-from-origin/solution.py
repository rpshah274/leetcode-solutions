# Problem: Furthest Point From Origin
# URL: https://leetcode.com/problems/furthest-point-from-origin/
# Language: python3

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        freq=Counter(moves)
        if freq['R']==freq['L']:
            return freq['_']
        else:
            return freq['_']+abs(freq['R']-freq['L'])