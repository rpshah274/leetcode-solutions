# Problem: Decode the Slanted Ciphertext
# URL: https://leetcode.com/problems/decode-the-slanted-ciphertext/
# Language: python3

class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        res = []
        if rows==1:
            return encodedText
        cols=int(len(encodedText)/rows)
        for start_col in range(cols):
            r, c = 0, start_col
            while r < rows and c < cols:
                res.append(encodedText[r*cols+c])
                r+=1
                c+=1
        return ''.join(res).rstrip()