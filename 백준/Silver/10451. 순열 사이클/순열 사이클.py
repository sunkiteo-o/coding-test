from collections import deque

t = int(input())

def dfs(start, visited, graph):
    q=deque()
    q.append(start)
    visited[start] = True

    while q:
        current = q.popleft()
        for next in graph[current]:
            if not visited[next]:
                visited[next] = True
                q.append(next)
    
    return 1


for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]

    for j in range(1,n+1):
        graph[j].append(arr[j-1])

    visited = [False] *(n+1)
    rst = 0

    for i in range(1,n+1):
        if not visited[i]:
            rst += dfs(i, visited, graph)

    print(rst)
