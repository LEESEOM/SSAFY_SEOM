# sw 13066 컨테이너 운반

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    power = list(map(int, input().split()))
    weight.sort(reverse=True)
    lift = 0
    bye = [0]*N
    for j in range(M):
        for i in range(N):
            if power[j]>=weight[i] and bye[i] == 0:
                lift += weight[i]
                bye[i] = 1
                break
            else:
                continue
    if lift == 0:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {lift}')
