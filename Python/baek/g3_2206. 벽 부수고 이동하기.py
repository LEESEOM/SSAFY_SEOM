# g3 2206 벽 부수고 이동하기
from collections import deque

dr = [0,0,1,-1]
dc = [1,-1,0,0]
def bfs(row,col,le,crash):
    qu = deque()
    qu.append((row,col,le,crash))
    visited[0][0][0] = 1
    while qu:
        row, col, le,crash = qu.popleft()
        if row == N-1 and col == M-1:
            return le
        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            if 0<=nr<N and 0<=nc<M:
                if maps[nr][nc] == 1 and crash == 0:
                    visited[nr][nc][1] = 1
                    qu.append((nr,nc,le+1,1))
                elif visited[nr][nc][crash] == 0 and maps[nr][nc] == 0:
                    visited[nr][nc][crash] = visited[row][col][crash] + 1
                    qu.append((nr,nc,le+1,crash))
    return -1


N, M = map(int, input().split())
maps = [list(map(int,input())) for _ in range(N)]
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
print(bfs(0,0,1,0))
