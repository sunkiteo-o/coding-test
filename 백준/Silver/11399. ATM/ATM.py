n = int(input())
p = list(map(int, input().split()))

p.sort()

sumArr = [0]*n
sumAll=0
for i in range(n):
    sumAll+=p[i]
    sumArr[i] = sumAll
    

print(sum(sumArr))
