# sw 13063 최소합

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dp_arr = [[0]*N for _ in range(N)]
    dp_arr[0][0] = arr[0][0]
    # 오른쪽, 아래쪽으로만 움직일 수 있다면
    # 왼쪽, 위쪽에서 왔다는 뜻
    for row in range(N):
        for col in range(N):
            if row == 0:
                dp_arr[row][col] = arr[row][col]+dp_arr[row][col-1]
            elif col == 0:
                dp_arr[row][col] = arr[row][col]+dp_arr[row-1][col]
            elif 0 <= row - 1 and 0 <= col - 1:
                dp_arr[row][col] = arr[row][col]+min(dp_arr[row-1][col], dp_arr[row][col-1])
    print(f'#{tc} {dp_arr[N-1][N-1]}')
