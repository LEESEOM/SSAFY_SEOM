# sw 10966 물놀이를 가자

from collections import deque

dr = [0,0,1,-1]
dc = [1,-1,0,0]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pool = [input() for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    cnt = 0
    qu = deque()
    for row in range(N):
        for col in range(M):
            if pool[row][col] == 'W':
                qu.append((row,col,1))
                visited[row][col] = 1
    while qu:
        a, b, count = qu.popleft()
        for i in range(4):
            nr = a + dr[i]
            nc = b + dc[i]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
                if pool[nr][nc] == 'L':
                    cnt += count
                    visited[nr][nc] = 1
                    qu.append((nr, nc, count+1))
    print(f'#{tc} {cnt}')
