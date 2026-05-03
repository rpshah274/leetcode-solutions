# Problem: Integers With Multiple Sum of Two Cubes
# URL: https://leetcode.com/problems/integers-with-multiple-sum-of-two-cubes/
# Language: python3

class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        count = Counter()
        res = []
        for i in range(1, 1100):
            for j in range(i, 1100):
                x = i**3 + j**3
                if x > n:
                    break
                count[x] += 1
                if count[x] == 2:
                    res.append(x)   
        return sorted(res)
                