# Problem: Majority Element
# URL: https://leetcode.com/problems/majority-element/
# Language: python3

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        Hashmap=collections.Counter(nums)
        max_key= max(Hashmap,key=Hashmap.get)
        return max_key