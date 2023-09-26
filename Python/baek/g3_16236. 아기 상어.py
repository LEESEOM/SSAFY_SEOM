# g3 16236 아기 상어
from collections import deque


dr = (0,0,1,-1)
dc = (1,-1,0,0)

N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]
time = 0
size = 2
cs = 0
x = y = 0
qu = deque()
# 상어 초기 위치
find = False
for row in range(N):
    if find:
        break
    else:
        for col in range(N):
            if space[row][col] == 9:
                space[row][col] = 0
                qu.append((row, col, 0))
                x, y = row, col # 초기 위치
                find = True
                break
# 먹이 결정 bfs
solo = True
while solo:
    menu = []
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1
    while qu:
        row, col, le = qu.popleft()
        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            if 0<=nr<N and 0<=nc<N and visited[nr][nc] == 0 and space[nr][nc] <= size:
                visited[nr][nc] = 1
                if 0 < space[nr][nc] < size:
                    menu.append((le+1,nr,nc))
                else:
                    qu.append((nr,nc,le+1))
    if not menu:
        solo = False
    else:
        menu.sort()
        le, x2, y2 = menu[0]
        space[x2][y2] = 0
        time += le
        qu.append((x2, y2, 0))
        x, y = x2, y2
        cs += 1
        if cs == size:
            cs = 0
            size += 1

print(time)