# Problem: Course Schedule II
# URL: https://leetcode.com/problems/course-schedule-ii/
# Language: python3

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre=defaultdict(list)
        for c,p in prerequisites:
            pre[c].append(p)
        taken=set()
        cycle=set()
        res=[]
        def dfs(course):
            if course in cycle:
                return False
            if course in taken:
                return True
            cycle.add(course)
            for p in pre[course]:
                if not dfs(p):
                    return False
            cycle.remove(course)
            taken.add(course)
            pre[course]=[]
            res.append(course)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return []
        return res