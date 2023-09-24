from collections import deque
from itertools import combinations

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

# 처음에 0인 녀석들의 (row, col)정보를 따로 저장해 두고
# 그냥 바이러스 위치도 고정이니 따로 빼두자
blank = []
virus = []
for row in range(N):
    for col in range(M):
        if arr[row][col] == 0:
            blank.append((row,col))
        elif arr[row][col] == 2:
            virus.append((row,col))
lst = list(combinations(blank,3))
# 조합을 통해 벽을 세우는 경우의 수 lst에 저장해두기
# N,M 이 최대 8이고 벽도 3개로 고정이라 돌려볼 만 한듯
# 이걸 가지고 조합 3번? 그냥 다 박아보면서 (bruteforce)
for i in range(len(lst)):
    # arr 깊은복사 해서 쓰는게 더 빠를 것 같음
    check = [item[:] for item in arr]
    for j in range(3):
        x, y = lst[i][j]
        check[x][y] = 1
    # 바이러스 시뮬레이션 돌려보고 (bfs)
    visited = [([0]*M) for _ in range(N)]
    for m in range(len(virus)):
        deq = deque()
        deq.append(virus[m])
        while deq:
            row, col = deq.popleft()
            for k in range(4):
                nr = row + dr[k]
                nc = col + dc[k]
                if 0<=nr<N and 0<=nc<M:
                    if check[nr][nc] == 0 and visited[nr][nc] == 0:
                        deq.append((nr,nc))
                        visited[nr][nc] = 1
                        check[nr][nc] = 2
    # 안전 구역 확인하고
    cnt = 0
    for row in range(N):
        for col in range(M):
            if check[row][col] == 0:
                cnt += 1
    # 최대면 갱신
    if cnt > ans:
        ans = cnt

# 다 돌리고 답 출력
print(ans)