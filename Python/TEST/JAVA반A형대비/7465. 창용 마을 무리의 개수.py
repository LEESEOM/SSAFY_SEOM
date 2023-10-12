from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*N for _ in range(N)]
    visited = [0]*N
    cnt = 0
    for i in range(M):
        x, y = map(int, input().split())
        arr[x-1][y-1] = arr[y-1][x-1] = 1
    deq = deque()
    for j in range(N):
        if visited[j] == 0:
            deq.append(j)
            visited[j] = 1
            cnt += 1
            while deq:
                now = deq.popleft()
                for k in range(N):
                    if arr[now][k] == 1 and visited[k] == 0:
                        deq.append(k)
                        visited[k] =1
    print(f'#{tc} {cnt}')