# Problem: Sum of Primes Between Number and Its Reverse
# URL: https://leetcode.com/problems/sum-of-primes-between-number-and-its-reverse/
# Language: python3

class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        r=int(str(n)[::-1])
        def is_prime(x):
            if x<2:
                return False
            if x==2:
                return True
            if x%2==0:
                return False
            for j in range(3,int(x**0.5)+1,2):
                if x%j==0:
                    return False
            return True
        total=0
        for i in range(min(n,r),max(n,r)+1):
            if is_prime(i):
                total+=i
        return total