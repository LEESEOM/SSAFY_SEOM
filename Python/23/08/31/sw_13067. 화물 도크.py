# sw 13067 화물 도크

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = []
    cnt = 0
    now = 0
    for i in range(N):
        s, e = map(int, input().split())
        lst.append([e,s])
    lst.sort()
    for j in range(N):
        if lst[j][1]>= now:
            cnt += 1
            now = lst[j][0]
    print(f'#{tc} {cnt}')
