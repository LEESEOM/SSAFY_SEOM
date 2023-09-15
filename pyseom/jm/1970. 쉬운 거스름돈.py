# sw 1970 쉬운 거스름돈

money = [50000,10000,5000,1000,500,100,50,10]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    check = [0]*8
    for i in range(N):
        if N < 10:
            break
        else:
            check[i] += N//money[i]
            N = N%money[i]
    print(f'#{tc}')
    print(*check)
