from collections import deque
from typing import List

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        graph = [[] for _ in range(n)]
        indegree = [0] * n
        costs = []

        for u, v, w in edges:
            graph[u].append((v, w))
            indegree[v] += 1
            costs.append(w)

        if not costs:
            return -1

        # Topological order
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        topo = []
        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        vals = sorted(set(costs))
        INF = 10 ** 30

        def check(limit):
            dist = [INF] * n
            dist[0] = 0

            for u in topo:
                if dist[u] == INF:
                    continue

                if u != 0 and u != n - 1 and not online[u]:
                    continue

                du = dist[u]

                for v, w in graph[u]:
                    if w < limit:
                        continue
                    if v != n - 1 and not online[v]:
                        continue
                    nd = du + w
                    if nd < dist[v]:
                        dist[v] = nd

            return dist[n - 1] <= k

        if not check(vals[0]):
            return -1

        lo, hi = 0, len(vals) - 1
        ans = vals[0]

        while lo <= hi:
            mid = (lo + hi) // 2
            if check(vals[mid]):
                ans = vals[mid]
                lo = mid + 1
            else:
                hi = mid - 1

        return ans