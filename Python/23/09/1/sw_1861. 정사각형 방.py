# sw 1861 정사각형 방

dr = [0,0,1,-1]
dc = [1,-1,0,0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    cnts = []
    for row in range(N):
        for col in range(N):
            now = room[row][col]
            cnt = 1
            done = True

            temp = [(row,col)]
            while temp:
                a, b = temp.pop()
                for i in range(4):
                    nr = a+dr[i]
                    nc = b+dc[i]
                    if 0<=nr<N and 0<=nc<N:
                        if room[nr][nc] == room[a][b]+1:
                            cnt += 1
                            temp.append((nr,nc))
                            break
            cnts.append([cnt,now])
    cnts.sort(reverse=True)
    for j in range(len(cnts)):
        if cnts[j][0] != cnts[j+1][0]:
            a = cnts[j]
            b = reversed(a)
            break
    print(f'#{tc}', *b)
