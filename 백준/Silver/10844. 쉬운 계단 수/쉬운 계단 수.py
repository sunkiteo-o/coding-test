n = int(input())
dp = [[0] *12 for _ in range(n+1)]

for i in range(2,11):
    dp[1][i] =1

for j in range(2,n+1):
    for k in range(1,11):
        dp[j][k] = dp[j-1][k-1] + dp[j-1][k+1]

ans = sum(dp[n])

print(ans%1000000000)