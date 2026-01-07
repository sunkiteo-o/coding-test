
from collections import deque
import sys
n, k = map(int,sys.stdin.readline().split())

count = 0 

visited = [False]*1000001

def find_brohter(n):
    q = deque()
    q.append([n,0])

    while q:
        n, count = q.popleft() 
        if n<1000001 and n>=0 and not visited[n]:
            count+=1
            visited[n]=True
            q.append([n*2, count])
            q.append([n+1, count])
            q.append([n-1, count])
            if n==k: 
                return count-1


rst = find_brohter(n)
print(rst)