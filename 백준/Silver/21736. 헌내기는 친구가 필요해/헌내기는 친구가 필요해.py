import sys
from collections import deque 
n,m = map(int,sys.stdin.readline().split())
campusMap = [list(sys.stdin.readline()) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

dist = [[0,-1],[0,1],[1,0],[-1,0]]

ans = 0

def bfs(sy,sx):
    q=deque()
    q.append((sy,sx))
    visited[sy][sx] = True
    cnt = 0

    while q:
        cy,cx = q.popleft()
        for dy,dx in dist:
            ny = dy+cy
            nx = dx+cx

            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and campusMap[ny][nx] !='X':
                visited[ny][nx] = True
                if campusMap[ny][nx] == 'P':
                    cnt+=1 
                q.append((ny,nx))
    return cnt


sy,sx= -1,-1
for i in range(n):
    for j in range(m):
        if campusMap[i][j] == 'I':
            sy,sx = i,j
            break
    if sy != -1:
         break

ans = bfs(sy,sx)

if ans==0: print('TT')
else: print(ans)



