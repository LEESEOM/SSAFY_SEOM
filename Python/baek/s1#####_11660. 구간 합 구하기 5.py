# N, M = map(int, input().split())
# chart = [list(map(int, input().split())) for _ in range(N)]
# sums = [list(map(int, input().split())) for _ in range(M)]
# dp = [[0]*N for _ in range(N)]
# dp[0][0] = chart[0][0]
# for row in range(N):
#     for col in range(N):
#         dp[row][col] =