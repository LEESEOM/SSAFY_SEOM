# di = [-1-1,0,1,1,1,0,-1]
# dj = [0,1,1,1,0,-1,-1,-1]
#
# T = int(input())
# for tc in range(1,T+1):
#     N, M = map(int, input().split())
#     # 기본 판 만들기
#     board = [[0] * N for _ in range(N)]
#     mid = N//2
#     board[mid][mid] = 2
#     board[mid-1][mid-1] = 2
#     board[mid-1][mid] = 1
#     board[mid][mid-1] = 1
#     # 돌 놓아보기
#     for _ in range(M):
#         c, r, color = map(int, input().split())
#         # 실제 놓아야 하는 위치는 c-1, r-1
#         board[r-1][c-1] = color
#         # 돌 놓았으니 방금 놓은 돌에 의해서 바뀌는 돌들 바꿔주기
#         # 8방향 탐색
#         i,j = r-1,c-1  # 현재위치
#         for d in range(8):
#             # 각 방향에 대해서 할 일