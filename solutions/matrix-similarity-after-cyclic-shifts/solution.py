# Problem: Matrix Similarity After Cyclic Shifts
# URL: https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/
# Language: python3

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        # n = len(mat[0])
        # k=k%n
        # for i, row in enumerate(mat):
        #     if i%2==0:
        #         shifted = row[k:]+row[:k]
        #     else:
        #         shifted = row[-k:]+row[:-k]
        #     if shifted != row:
        #         return False
        # return True
        m,n=len(mat),len(mat[0])
        if k%n==0:
            return True
        k=k%n
        count_good_rows=0
        for i in range(m):
            if i%2==0:
                #Left Shift
                for j in range(n):
                    idx=(k+j)%(n)
                    if mat[i][j]!=mat[i][idx]:
                        return False
            else: 
                #Right Shift
                for j in range(n):
                    idx=(j-k)%(n)
                    if mat[i][j]!=mat[i][idx]:
                        return False
        return True