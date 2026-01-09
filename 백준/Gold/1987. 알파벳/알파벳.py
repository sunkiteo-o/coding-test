import sys
r,c = map(int,sys.stdin.readline().split())
chaMap = [list(sys.stdin.readline()) for _ in range(r)]

dist = [[0,-1],[0,1],[1,0],[-1,0]]
chk = set()

ans = 0

def dfs(y,x,cnt):
    global ans
    ans = max(cnt,ans)

    for dy,dx in dist:
        ny = dy+y
        nx = dx+x

        if 0 <= ny < r and 0 <= nx < c and chaMap[ny][nx] not in chk:
            chk.add(chaMap[ny][nx])
            dfs(ny,nx, cnt+1)
            chk.remove(chaMap[ny][nx])


chk.add(chaMap[0][0])
dfs(0,0,1)
print(ans)



