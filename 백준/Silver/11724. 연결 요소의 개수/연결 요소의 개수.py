from collections import deque 
import sys

n, m = map(int, input().split())

visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(graph, visited, start):
    q = deque()
    q.append(start)
    visited[start] = True

    while(q):
        current = q.popleft()

        for next in graph[current]:
            if not visited[next]: 
                visited[next] = True
                q.append(next)
    
rst = 0
for i in range(1,n+1):
    if visited[i] == False: 
        dfs(graph, visited, i)
        rst+=1

print(rst)

