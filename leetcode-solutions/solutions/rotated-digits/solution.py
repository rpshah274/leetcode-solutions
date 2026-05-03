# Problem: Rotated Digits
# URL: https://leetcode.com/problems/rotated-digits/
# Language: python3

class Solution:
    def rotatedDigits(self, n: int) -> int:
        good={2,5,6,9}
        bad={3,4,7}
        def is_good(num):
            good_d=0
            while num > 0:
                digit = num % 10
                if digit in bad:
                    return False
                if digit in good:
                    good_d+=1
                num = num // 10
            return True if good_d>0 else False
        count=0
        for i in range(1,n+1):
            if is_good(i):
                count+=1
        return count