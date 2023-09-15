# sw_12675_배열최소합

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 0
    for i in range(N):
        min_row = 10
        for j in range(N):
            if arr[i][j] < min_row:
                min_row = arr[i][j]
        min_sum += min_row
    print(f'#{tc} {min_sum}')