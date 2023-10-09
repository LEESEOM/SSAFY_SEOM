from collections import deque

dr = [0,0,1,-1]
dc = [1,-1,0,0]

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

deq = deque()
deq.append((0,0,1))

while deq:
    row, col, cnt = deq.popleft()
    if row == N-1 and col == M-1:
        print(cnt)
        break
    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        if 0<=nr<N and 0<=nc<M and maze[nr][nc] and not visited[nr][nc]:
            visited[nr][nc] = 1
            deq.append((nr, nc, cnt + 1))
