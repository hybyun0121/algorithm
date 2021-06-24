from types import *
class Solution:
    from collections import defaultdict, deque
    def findCheapestPrice(self, n, flights, src, dst, k):
        total = defaultdict(list)
        graph = defaultdict(list)
        q = deque()
        hop = 0

        for u, v, p in flights:
            graph[u].append((v,p))

        q.append((0, src))
        visited = []

        while q:
            if hop <= k+1:
                price, node = q.popleft()
                if node not in visited:
                    visited.append(node)
                    total[node].append(price)
                    hop += 1
                    for i, (v, p) in enumerate(graph[node]):
                        q.append((price+p, v))
                    hop -= i
            else:
                break


        try:
            dst_price = total[dst]
            return min(dst_price)
        except:
            return -1

sol = Solution()
flights = [[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]]

sol.findCheapestPrice(n = 10, flights = flights,
                        src = 6, dst = 0, k = 7)
