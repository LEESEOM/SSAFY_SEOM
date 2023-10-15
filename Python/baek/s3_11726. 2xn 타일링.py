n = int(input())

dp = [[0] for _ in range(n+1)]
dp[0], dp[1] = 1, 2
for i in range(2, n):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[n-1])
