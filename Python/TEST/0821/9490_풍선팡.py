dr = [0,0,1,-1]
dc = [1,-1,0,0]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_pang = 0
    for row in range(N):
        for col in range(M):
            cnt = arr[row][col]
            for i in range(4):
                for j in range(1,arr[row][col]+1):  # cnt를 넣어버리면
                    nr = row + dr[i]*j
                    nc = col + dc[i]*j
                    if 0<=nr<N and 0<=nc<M:
                        cnt += arr[nr][nc]
                if cnt > max_pang:
                    max_pang = cnt
    print(f'#{tc} {max_pang}')


