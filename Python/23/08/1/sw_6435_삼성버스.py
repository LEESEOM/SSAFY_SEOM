# 6485 D3
# 삼성시의 버스 노선

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    stops = [0] * 5001  # 각 정류장에 몇개의 노선이 다니는지 숫자 세기
    for _ in range(N):
        A, B = map(int, input().split())  # 버스 노선
        for i in range(A, B+1):
            stops[i] += 1
    P = int(input())
    print(f'#{tc}',end=' ')
    for _ in range(P):
        num = int(input())  # 몇 개의 노선이 거치는지 확인할 정류장의 번호
        print(stops[num],end=' ')
    print()