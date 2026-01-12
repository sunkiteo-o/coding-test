n = int(input())

lst = [0]+ list(map(int,input().split()))

dp = [0]*(n+1)

for i in range(n,0,-1):
    maxValue= 0
    for j in range(n,i,-1):
        if lst[i]>lst[j]:
            maxValue = max(maxValue,dp[j])

    dp[i] = maxValue + 1

print(max(dp))
