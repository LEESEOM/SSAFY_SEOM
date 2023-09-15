# 삼성시의 버스 노선

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    road = [0] * 5001
    for _ in range(N):
        a, b = map(int, input().split())
        for j in range(a, b+1):
            road[j] += 1
    P = int(input())
    print(f'#{tc}',end=" ")
    for _ in range(P):
        num = int(input())
        print((road[num]),end=' ')
        
        #? 왜틀림