# sw 1860 진기의 최고급 붕어빵

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    time = list(map(int, input().split()))
    time.sort()
    bbang = 0
    now = 0
    b = 0
    is_impos = False
    while time:
        new = time.pop(0)
        a = new - now
        now = new
        bbang += K*((a+b)//M)
        b = (a+b)%M
        bbang -= 1
        if bbang < 0:
            print(f'#{tc} Impossible')
            is_impos = True
            break
    if not is_impos:
        print(f'#{tc} Possible')

