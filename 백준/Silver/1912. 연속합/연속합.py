import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))

cur = ans = arr[0]
for x in arr[1:]:
    cur = max(x, cur + x)
    ans = max(ans, cur)

print(ans)
