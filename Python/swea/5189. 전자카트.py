def cheap(now,cost,cnt):
    global min_cost
    # 모두 다 돌았으면 비교하고 종료
    if cnt == N-1:
        # 자기 자리로 오는거 더해주고
        cost += arr[now][0]
        if cost < min_cost:
            min_cost = cost
        return
    # 모든 자리 보면서 재귀로
    for i in range(1,N):
        if visited[i] == 0:
            visited[i] = 1
            cheap(i,cost+arr[now][i],cnt+1)
            visited[i] = 0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_cost = 100*N # 100 이하니까
    visited = [0]*N
    cheap(0,0,0)
    print(f'#{tc} {min_cost}')
