# sw 1926 간단한 369게임

N = int(input())
for i in range(1,N+1):
    cnt = 0
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        for j in str(i):
            if '3' == j or '6' == j or '9' == j:
                cnt += 1
        print(f'{"-"*cnt}',end=" ")
    else:
        print(i,end=" ")