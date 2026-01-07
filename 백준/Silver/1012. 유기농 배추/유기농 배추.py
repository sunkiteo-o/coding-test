from collections import deque

t = int(input())
dist = [[-1,0],[1,0],[0,-1],[0,1]]


def bfs(y,x):
    q= deque()
    q.append((y,x))
    visited[y][x]=True

    while q:
        y,x = q.popleft()

        for d in dist:
            ny = y+d[0]
            nx = x+d[1]
            if 0<= ny<n and 0<=nx<m:
                if baechu[ny][nx]==1 and not visited[ny][nx]:
                    visited[ny][nx]=True
                    q.append((ny,nx))
    return 1

for _ in range(t):
    m,n,k = map(int,input().split())

    arr = [list(map(int,input().split())) for _ in range(k)]
    visited = [[False]*m for _ in range(n)]
    baechu = [[0]*m for _ in range(n)]
    count = 0

    for a in arr:
        x,y=a[0],a[1]
        baechu[y][x] =1
    
    for i in range(n):
        for j in range(m):
            if baechu[i][j] ==1 and not visited[i][j]:
                count +=bfs(i,j)

    print(count)
