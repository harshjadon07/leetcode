from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ans = 0

        def dfs(node, comp):
            visited[node] = True
            comp.append(node)
            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei, comp)

        for i in range(n):
            if not visited[i]:
                comp = []
                dfs(i, comp)

                vertices = len(comp)
                edge_count = 0
                for node in comp:
                    edge_count += len(graph[node])
                edge_count //= 2

                if edge_count == vertices * (vertices - 1) // 2:
                    ans += 1

        return ans