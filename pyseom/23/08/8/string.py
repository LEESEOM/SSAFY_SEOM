# sw 1213 .
# [S/W 문제해결 기본] 3일차 - String

for tc in range(1, 11):
    T = int(input())
    N = input()
    M = input()
    print(f'#{tc} {len(M.split(N))-1}')
