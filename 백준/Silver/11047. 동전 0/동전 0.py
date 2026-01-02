n, k = map(int, input().split())
mapA = []
count = 0

for i in range(n):
    mapA.append(int(input()))

mapA.reverse()

for coin in mapA:
    count += k//coin
    k %= coin 

print(count)