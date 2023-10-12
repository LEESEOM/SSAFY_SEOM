def dfs(idx,high):
    global min_dif
    if high >= min_dif:
        return
    if idx >= N:
        if high >= B:
            min_dif = high
        return
    visited[idx] += 1
    dfs(idx+1, high + height[idx])
    visited[idx] -= 1
    dfs(idx+1, high)

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    height.sort(reverse=True)
    min_dif = 10000*N
    visited = [0]*N
    dfs(0,0)
    print(f'#{tc} {abs(B-min_dif)}')
