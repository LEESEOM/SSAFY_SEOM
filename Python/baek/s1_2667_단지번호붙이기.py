# S1 2667 단지번호붙이기

dr = [0,0,1,-1]
dc = [1,-1,0,0]
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
cnt = 0  # 단지수 넣을 것
lst = [] # 단지 내 집 수 넣을 것
for row in range(N):
    for col in range(N):
        if arr[row][col] == 1 and visited[row][col] == 0:
            visited[row][col] = 1
            cnt += 1
            hcnt = 10
            queue = []
            queue.append((row,col))
            while queue:
                r, c = queue.pop(0)
                for i in range(4):
                    cr = r + dr[i]
                    cc = c + dc[i]
                    if 0<=cr<N and 0<=cc<N:
                        if arr[cr][cc] == 1 and visited[cr][cc] == 0:
                            queue.append((cr,cc))
                            hcnt += 1
                            visited[cr][cc] = 1
            lst.append(hcnt)
print(cnt)
lst.sort()
for j in range(len(lst)):
    print(lst[j])