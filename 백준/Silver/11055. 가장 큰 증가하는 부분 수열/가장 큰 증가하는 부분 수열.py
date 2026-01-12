n = int(input())
lst = [0]+list(map(int,input().split()))

dp = [0]*(n+1)
ans = 0

for i in range(1,n+1):
    maxValue = 0
    for j in range(1,i):
        if lst[i]>lst[j]:
            maxValue = max(maxValue, dp[j])

    dp[i] = lst[i]+maxValue

print(max(dp))
    




