from collections import deque


dr = (0, 0, 1, -1)
dc = (1, -1, 0, 0)
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    qu = deque()
    qu.append([0, 0, 0])
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    while qu:
        row, col, cnt = qu.popleft()
        if row == n-1 and col == m-1:
            return cnt+1
        else:
            for i in range(4):
                nr = row + dr[i]
                nc = col + dc[i]
                if 0<=nr<n and 0<=nc<m and visited[nr][nc] == 0:
                    if maps[nr][nc] == 1:
                        visited[nr][nc] = 1
                        qu.append([nr,nc,cnt+1])
    return -1