# sw 1220 Magnetic

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    for col in range(N):
        now = 2
        for row in range(N):
            if arr[row][col] == 1:
                now = 1
            if arr[row][col] == 2 and now == 1:
                cnt += 1
                now = 2
    print(f'#{tc} {cnt}')


# T = 10
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     cnt = 0
#     now = 2
#     for col in range(N):
#         is_find = False
#         for row in range(N):
#             if is_find:
#                 break
#             if arr[row][col] == 1:
#                 now = 1
#                 is_find = True
#                 while row != N:
#                     if now == 1 and arr[row][col] == 2:
#                         now = 2
#                         cnt += 1
#                     if now == 2 and arr[row][col] == 1:
#                         now = 1
#                     row += 1
#                 now = 2
#     print(f'#{tc} {cnt}')