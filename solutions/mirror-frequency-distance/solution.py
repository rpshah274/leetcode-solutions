# Problem: Mirror Frequency Distance
# URL: https://leetcode.com/problems/mirror-frequency-distance/
# Language: python3

class Solution:
    def mirrorFrequency(self, s: str) -> int:
        freq_l=[0]*26
        freq_d=[0]*10
        for ch in s:
            if 'a'<=ch<='z':
                freq_l[ord(ch)-ord('a')]+=1
            else:
                freq_d[int(ch)]+=1
        res=0
        for i in range(13):
            res += abs(freq_l[i] - freq_l[25 - i])
        for i in range(5):
            res += abs(freq_d[i] - freq_d[9 - i])
        return res            