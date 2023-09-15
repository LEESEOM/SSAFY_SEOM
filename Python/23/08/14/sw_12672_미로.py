di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    check = [[0] * N for _ in range(N)]
    stack = []
    info = (0, 0)
    start = 0
    # 시작점 (2위치) 찾기
    for s in range(N):
        if maze[N][s] == 2:
            check[N][s] = 1
            info = (N, s)
            start = s
            stack.append(info)
    while stack:
        for i in range(4):       # 스택에 뭘 저장해야하지
            try:                 # ??
                if maze[N+di[i]][s+dj[i]] == 0 and check[N+di[i]][s+dj[i]] != 1:
                    N, s = N+di[i], s+dj[i]
                    check[N][s] = 1
                    stack.append(info)

            except IndexError:
                continue

