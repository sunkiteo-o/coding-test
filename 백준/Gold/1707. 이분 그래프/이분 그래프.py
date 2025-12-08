from collections import deque
import sys

# 입력 
k = int(input())
colors = ['R','G']

def chg_color(n,visited):
    if visited[n] == 'R':
        return 'G'
    else:
        return 'R'


def dfs(graph, visited, start):
    q= deque()
    q.append(start)
    visited[start] = colors[0]

    while q:
        current = q.popleft()
        color = chg_color(current,visited)

        # color가 전환되어야 함. 
        for next in graph[current]:
            # 컬러 비교 
            # 기존 컬러랑 여기 컬러가 같으면 ok 다르면 no 
            if visited[next] != False and visited[next] != color:
                return 'NO'
            if not visited[next]:
                q.append(next)
                visited[next] = color
    return 'YES'


for _ in range(k):
    v, e = map(int,input().split())
    graph = [[] for _ in range(v+1)]
    visited = [False] *(v+1)

    for _ in range(e):
        u,v = map(int, sys.stdin.readline().split())
        # u,v=map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    for i in range(1,v+1):
        if not visited[i]:
            rst = dfs(graph, visited, i)
            if rst == 'NO':
                break
    print(rst)

    
    

