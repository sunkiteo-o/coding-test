# 상하좌우 
# 1 익은 0 토마토 -1 빈 칸

import sys
from collections import deque
dist = [[0,-1],[0,1],[1,0],[-1,0]]

m, n = map(int,input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
q=deque()

for sy in range(n):
    for sx in range(m):
        if arr[sy][sx] == 1 and not visited[sy][sx]:
            q.append([sy,sx])
            visited[sy][sx]=True

while q:
    cy,cx = q.popleft()
    for dy,dx in dist:
        ny= cy+dy
        nx = cx+dx
        if 0<=ny<n and 0<=nx<m and arr[ny][nx] ==0 and visited[ny][nx] == False:
            arr[ny][nx] = arr[cy][cx]+1
            visited[ny][nx] = True
            q.append([ny,nx])


ans=0
for line in arr:
    for tomato in line:
        if tomato ==0:
            print(-1)
            exit()
    ans = max(ans,max(line))

print(ans-1)

