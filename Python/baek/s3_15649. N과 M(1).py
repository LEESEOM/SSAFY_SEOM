def perm(lst):
    if len(lst) == M:
        print(*lst)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            perm(lst + [arr[i]])
            visited[i] = 0


N, M = map(int, input().split())
arr = [x for x in range(1,N+1)]
visited = [0]*N
perm([])

