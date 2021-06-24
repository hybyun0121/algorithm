import collections

# Sol 01 재귀적으로 풀기
'''
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        route = []
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop())
            route.append(a)

        dfs('JFK')
        return route[::-1]
'''

# Sol 02 반복으로 풀기
def findItinerary(tickets):
    graph = collections.defaultdict(list)
    for a,b in sorted(tickets):
        graph[a].append(b)

    print(graph)
    route, stack = [], ['JFK']
    while stack:
        # 반복으로 스택을 구성하되 막히는 부분에서 풀어내는 처리
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop(0))
            print(f"stack : {stack}")

        route.append(stack.pop())
        print(f"route : {route}")

    return route[::-1]

tickets = [["JFK", "KUL"],["JFK", "NRT"], ["NRT", "JFK"]]
print(findItinerary(tickets))
