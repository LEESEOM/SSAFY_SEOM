# def dfs(h, le):
#     if # cant move:
#         if le > max_len:
#             max_len = le
#         for i in range(4):
#             nr = row + dr[i]
#             nc = col + dc[i]
#             if 0<=nr<N and 0<=nc<N:
#                 if info[nr][nc] <= info[row][col]:
#                     # 넣고
#                 elif info[nr][nc]
#
#     pass
#
# dr = [0,0,1,-1]
# dc = [1,-1,0,0]
#
# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     info = [list(map(int, input().split())) for _ in range(N)]
#     dig = 1
#     max_len = 0
#     max_height = 0
#     # 최고점들 찾아서 좌표 저장하기
#     for row in range(N):
#         for col in range(N):
#     # 만약 최고점이 1개라면 2번째 최고점 찾아서 거기도 확인해야함
