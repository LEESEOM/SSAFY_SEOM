T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(N)]
    arr90 = [[0]*N for _ in range(N)]
    arr180 = [[0] * N for _ in range(N)]
    arr270 = [[0] * N for _ in range(N)]
    ans = []
    print(f'#{tc}')
    for k in range(3):                        # 3번 굴릴 것
        for i in range(N):
            for j in range(N):
                arr90[i][j] = arr[N-1-j][i]     # 90도 돌리는 방법
    for k in range(3):
        for i in range(N):
            for j in range(N):
                arr180[i][j] = arr90[N - 1 - j][i]      # 그걸 90도
    for k in range(3):
        for i in range(N):
            for j in range(N):
                arr270[i][j] = arr180[N - 1 - j][i]   # 그걸 90도
    for m in range(N):
        print(f"{''.join(arr90[m])} {''.join(arr180[m])} {''.join(arr270[m])}")
