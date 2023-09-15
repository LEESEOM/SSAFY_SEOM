def route(sr,sc):
    stack.append((sr,sc))
    while stack:
        row, col = stack.pop(0)
        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            if 0<=nr<16 and 0<=nc<16:
                if maze[nr][nc] == 3:
                    return 1
                if maze[nr][nc] == 0 and visited[nr][nc] == 0:
                    stack.append((nr, nc))
                    visited[nr][nc] += 1
    return 0


dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
for tc in range(1, 11):
    T = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    visited = [[0]*16 for _ in range(16)]
    stack = []
    # 시작점 찾기
    for row in range(16):
        for col in range(16):
            if maze[row][col] == 2:
                sr, sc = row, col
                break
    print(f'#{tc} {route(sr,sc)}')
