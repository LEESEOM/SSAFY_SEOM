from collections import deque

N, M = map(int, input().split())
arr = [[0]*N for _ in range(N)]
visited = [0]*N
cnt = 0
# 그래프에 연결 정보 표시
for i in range(M):
    u, v = map(int, input().split())
    arr[u-1][v-1] = arr[v-1][u-1] = 1
# 1번부터 돌면서 연결된거 다 visited 체크하고
# 새로운 출발점일 때는 cnt 1씩 추가
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
print(cnt)
