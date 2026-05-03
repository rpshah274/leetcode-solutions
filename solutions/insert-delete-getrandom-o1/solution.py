# Problem: Insert Delete GetRandom O(1)
# URL: https://leetcode.com/problems/insert-delete-getrandom-o1/
# Language: python3

import random
class RandomizedSet:
    def __init__(self):
        self.arr=[]
        self.rand={}

    def insert(self, val: int) -> bool:
        if val in self.rand:
            return False
        self.rand[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.rand:
            return False

        index = self.rand[val]
        last_val = self.arr[-1]

        # Swap val to last element
        self.arr[index] = last_val
        self.rand[last_val] = index

        # Remove element
        self.arr.pop()
        del self.rand[val]
        return True

    def getRandom(self) -> int:
        return random.choice(list(self.arr))

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()