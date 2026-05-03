# Problem: Lemonade Change
# URL: https://leetcode.com/problems/lemonade-change/
# Language: python3

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count_5=0
        count_10=0
        count_20=0
        for n in bills:
            if n==5:
                count_5+=1
            elif n==10:
                if count_5==0:
                    return False
                count_5-=1
                count_10+=1
            else:
                if not (count_5>=3 or (count_5>=1 and count_10>=1)):
                    return False
                elif (count_5>=1 and count_10>=1):
                    count_5-=1
                    count_10-=1
                    count_20+=1
                elif count_5>=3:
                    count_5-=3
                    count_20+=1
        return True