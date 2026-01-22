n= int(input())

lst = [0]+list(map(int,input().split()))

dp = [-1000]*(n+1)

for i in range(1,n+1):
    if lst[i] + dp[i-1] >= lst[i]:
        dp[i]=lst[i] + dp[i-1]
    else: 
        dp[i]=lst[i]


print(max(dp))