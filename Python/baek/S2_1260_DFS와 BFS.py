def dfs(V):
    visited[V] = 1
    print(V,end=" ")
    for j in range(N+1):
        if info[V][j] == 1 and visited[j] == 0:
            dfs(j)


def bfs(V):
    queue = [V]
    bfs_lst = []
    visited = [0]*(N+1)
    visited[V] = 1
    while queue:
        t = queue.pop(0)
        bfs_lst.append(t)
        for k in range(N+1):
            if info[t][k] == 1 and visited[k] == 0:
                queue.append(k)
                visited[k] = 1
    return bfs_lst


N, M, V = map(int, input().split())
info = [[0]*(N+1) for _ in range(N+1)]
visited = [0] * (N + 1)
for i in range(M):
    a, b = map(int,input().split())
    info[a][b] = info[b][a] = 1
dfs(V)
print()
print(*bfs(V))
