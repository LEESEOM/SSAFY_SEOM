# sw_12718_미로의 거리

def route(r, c):
    queue = [(r,c)]
    while queue:
        cr, cc = queue.pop(0)
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0<=nr<N and 0<=nc<N:
                if maze[nr][nc] == 3:
                    return visited[cr][cc]
                elif maze[nr][nc] == 0 and visited[nr][nc] == 0:
                    visited[nr][nc] = visited[cr][cc] + 1
                    queue.append((nr,nc))
    return 0

dr = [0,0,1,-1]
dc = [1,-1,0,0]
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    # 시작점 찾기
    for row in range(N):
        for col in range(N):
            if maze[row][col] == 2:
                x, y = row, col
    print(f'#{tc} {route(x, y)}')


