N = int(input())
M = int(input())
bus = [list(map(int, input().split())) for _ in range(M)]
A, B = map(int, input().split())
bus.sort()
dp = [0]*(A+1)+[100000000]*(N-A)
for i in range(M):
    start, end, cost = bus[i]
    if start >= A and end >= A:
        if dp[start] > dp[end]:
            if dp[start]+cost < dp[end]:
                dp[end] = dp[start]+cost
        if dp[start] < dp[end]:
            if dp[end]+cost < dp[start]:
                dp[start] = dp[end]+cost
print(dp[B])
# 으아ㅏ아아아ㅏㄱ
