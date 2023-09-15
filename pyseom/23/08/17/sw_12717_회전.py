# sw_12717_회전

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    suyeol = list(map(int, input().split()))
    answer = suyeol[M%N]
    print(f'#{tc} {answer}')
