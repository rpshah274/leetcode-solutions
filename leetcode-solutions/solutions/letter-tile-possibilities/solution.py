# Problem: Letter Tile Possibilities
# URL: https://leetcode.com/problems/letter-tile-possibilities/
# Language: python3

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        freq = [0] * 26
        for ch in tiles:
            freq[ord(ch) - ord('A')] += 1
        def backtrack():
            total = 0
            for i in range(26):
                if freq[i] > 0:
                    total += 1
                    freq[i] -= 1
                    total += backtrack()
                    freq[i] += 1
            return total
        return backtrack()