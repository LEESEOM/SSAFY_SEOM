# sw 1953 탈주범 검거
from collections import deque

info = [[],[(1,0),(-1,0),(0,1),(0,-1)],[(1,0),(-1,0)],[(0,1),(0,-1)],[(-1,0),(0,1)],[(1,0),(0,1)],[(1,0),(-1,0)],[(-1,0),(-1,0)]]

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    connect = [[0]*M for _ in range(N)]
    # 방향대로 연결정보 해놓고
    stack = deque()
    stack.append((R,C,1))
    connect[R][C] = 1
    while stack:
        row, col, le = stack.popleft()
        for i in range(len(info[tunnel[row][col]])):
            nr = row + info[tunnel[row][col]][i][0]
            nc = col + info[tunnel[row][col]][i][1]
            if 0<=nr<N and 0<=nc<M and connect[nr][nc] == 0:
                connect[nr][nc] = le+1
                stack.append((nr, nc, le+1))
                # 이동할 곳도 연결되어 있는지 확인해야 함
    cnt = 0
    for row in range(N):
        for col in range(M):
            if connect[row][col] <= L:
                cnt +=1
    print(f'#{tc} {cnt}')