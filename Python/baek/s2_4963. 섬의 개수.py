from collections import deque

d = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    maps = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    cnt = 0
    # 그냥 8방향 bfs
    deq = deque()
    for row in range(h):
        for col in range(w):
            if maps[row][col] and not visited[row][col]:
                deq.append((row,col))
                visited[row][col] = 1
                cnt += 1
                while deq:
                    r, c = deq.popleft()
                    for i in range(8):
                        dr, dc = d[i]
                        nr = r + dr
                        nc = c + dc
                        if 0<=nr<h and 0<=nc<w:
                            if maps[nr][nc] and not visited[nr][nc]:
                                visited[nr][nc] = 1
                                deq.append((nr,nc))
    print(cnt)
