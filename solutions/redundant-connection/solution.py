# Problem: Redundant Connection
# URL: https://leetcode.com/problems/redundant-connection/
# Language: python3

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #TOPO Pruning
        n = len(edges)
        graph = defaultdict(list)
        indegree=[0]*(n+1)
        for s,d in edges:
            graph[d].append(s)
            indegree[d]+=1
            graph[s].append(d)
            indegree[s]+=1
        q=deque()
        for i in range(1,n+1):
            if indegree[i]==1:
                q.append(i)
        visited=[False] * (n + 1) 

        while q:
            node=q.popleft()
            indegree[node] -= 1
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei]==1:
                    q.append(nei)

        for s,d in reversed(edges):
            if indegree[s]==2 and indegree[d]:
                return[s,d]
        return []