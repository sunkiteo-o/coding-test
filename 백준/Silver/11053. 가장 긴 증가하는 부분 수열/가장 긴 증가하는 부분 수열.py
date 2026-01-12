n = int(input())

lst =  [0] + list(map(int,input().split()))

dp = [0]*(n+1)

for i in range(1,n+1):
    maxValue = 0
    for j in range(0,i):
        if lst[j] < lst[i]:
            maxValue =max(maxValue,dp[j])
    
    dp[i]=maxValue+1

print(max(dp))
