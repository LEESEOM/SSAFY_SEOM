# 12467 전기 버스

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    loc = 0
    arr = [0] * (N+1)
    charge = list(map(int, input().split()))
    for j in charge:
        arr[j] += 1
    cnt = 0
    while loc < N:
        now_spot = loc
        for i in range(K, 0, -1):
            if loc + K >= N:
                loc = N
                break
            elif arr[loc + i] == 1:
                loc = loc + i
                cnt += 1
                break
        if loc >= N:
            print(f'#{tc} {cnt}')
            break
        if loc == now_spot:
            print(f'#{tc} 0')
            break