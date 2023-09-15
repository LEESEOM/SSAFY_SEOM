# sw 13065 전자카트

def cheap(loca, cost, cnt):
    global min_cost
    global visited
    global info
    global N
    if cnt == N-1:
        cost += info[loca][0]
        if cost < min_cost:
            min_cost = cost
        return
    for j in range(1, N):
        if visited[j] == 0:
            visited[j] += 1
            cheap(j ,cost+info[loca][j], cnt+1)
            visited[j] -= 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]
    min_cost = 100*N
    visited = [0]*N
    cheap(0, 0, 0)
    print(f'#{tc} {min_cost}')
