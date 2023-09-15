# 마름모 이동할 델타
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_num = 0
    benefit = 0
    cnt = 0
    for row in range(N):
        for col in range(N):
            for K in range(1, 24):
                cost = K * K + (K - 1) * (K - 1)
                benefit -= cost
                cnt = 0
                # 여기서 마름모 범위로
                #     nr = row + dr[i]
                #     nc = col + dc[i]
                #     if 0<=nr<N and 0<=nc<N:
                        if arr[nr][nc] == 1:
                            benefit += M
                            cnt += 1
                if benefit >= 0:
                    if cnt > max_num:
                        max_num = cnt
                        benefit = 0

    print(f'#{tc} {max_num}')



    # 1 ~ k = 24 보단 작다~



    # 집 들의 수