T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    # 가로
    for row in range(N):
        for col in range(N):
            if puzzle[row][col] == 1:
                cnt = 0
                if col > 0:
                    if puzzle[row][col-1] == 1:
                        continue
                while 0<=col<N and puzzle[row][col] == 1:
                    cnt += 1
                    col += 1
                if cnt == K:
                    ans += 1
    # 세로
    for col in range(N):
        for row in range(N):
            if puzzle[row][col] == 1:
                cnt = 0
                if row > 0:
                    if puzzle[row-1][col] == 1:
                        continue
                while 0 <= row < N and puzzle[row][col] == 1:
                    cnt += 1
                    row += 1
                if cnt == K:
                    ans += 1
    print(f'#{tc} {ans}')