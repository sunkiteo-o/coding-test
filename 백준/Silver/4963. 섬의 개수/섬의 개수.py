from collections import deque
import sys

# 섬인지 체크하는 함수 chk_land

# 상하좌우, 대각선 배열
dist = [[-1,-1],[-1,0],[-1,1],
        [0,-1], [0,1],
        [1,-1],[1,0],[1,1]]


# 섬의 개수 찾는 함수 dfs 
def dfs(arr,visited,sy,sx,w,h):
    q = deque()
    q.append([sy,sx])
    visited[sy][sx] = True

    while q:
        cy, cx = q.popleft()
        

        # 상하좌우, 대각선 탐색
        for dy,dx in dist:
            ny = cy+dy
            nx = cx+dx

            if 0<=ny<h and 0<=nx<w and not visited[ny][nx] and arr[ny][nx]==1:
                visited[ny][nx] = True
                q.append([ny,nx])
                
    return 1

        
# 00 이면 입력 종료 
while True:
    w,h = map(int, input().split())
    if w==0 and h==0:
        break
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    visited = [list(False for _ in range(w)) for _ in range(h)]
    rst = 0

    for sy in range(h):
        for sx in range(w):
            if not visited[sy][sx] and arr[sy][sx]==1: 
                rst += dfs(arr, visited, sy,sx,w,h)
    print(rst)
