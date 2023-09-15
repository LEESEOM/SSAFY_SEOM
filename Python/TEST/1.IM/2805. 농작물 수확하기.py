# sw 2805 농작물 수확하기

dr = [0,0,1,-1]
dc = [1,-1,0,0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    midrow = midcol = N//2
    benefit = farm[midrow][midcol]
    visited = [[0]*(N+1) for _ in range(N+1)]
    qu = [(midrow, midcol)]
    visited[midrow][midcol] = 1
    while True:
        if not qu:
            break
        row, col = qu.pop(0)
        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            if 0<=nr<N and 0<=nc<N and visited[nr][nc] == 0:
                visited[nr][nc] = visited[row][col] + 1
                if visited[nr][nc] <= N//2:
                    qu.append((nr, nc))
                benefit += farm[nr][nc]
    print(f'#{tc} {benefit}')


