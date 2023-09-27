import collections

dr = [0,0,1,-1]
dc = [1,-1,0,0]
M, N = map(int,input().split())
info = [list(map(int,input().split())) for _ in range(N)]
ik = [[-1]*M for _ in range(N)]
max_day = 0
for row in range(N):
    for col in range(M):
        if info[row][col] != 0:
            ik[row][col] = 0

deq = collections.deque()

for row in range(N):
    for col in range(M):
        if info[row][col] == 1:
            deq.append((row,col))
while deq:
    r, c = deq.popleft()
    for i in range(4):
        cr = r + dr[i]
        cc = c + dc[i]
        if 0<=cr<N and 0<=cc<M:
            if info[cr][cc] == 0 and ik[cr][cc] == -1:
                deq.append((cr, cc))
                ik[cr][cc] = ik[r][c] + 1

# 다시 확인했을 떄
is_hi = True
for row in range(N):
    for col in range(M):
        if ik[row][col] == -1:
            print(-1)
            is_hi = False
            break
        if ik[row][col] > max_day:
            max_day = ik[row][col]
    if not is_hi:
        break
if is_hi:
    print(max_day)