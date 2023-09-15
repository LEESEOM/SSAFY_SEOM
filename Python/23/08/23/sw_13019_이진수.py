# sw 13019 이진수

T = int(input())
for tc in range(1, T+1):
    N, Hex = input().split()
    a = bin(int(Hex, base=16))
    if len(a)%2 == 0:
        print(f'#{tc} {a[2:]}')
    else:
        print(f'#{tc} 0{a[2:]}')

