# sw 5356 의석이의 세로로 말해요

T = int(input())
for tc in range(1, T+1):
    arr = [list(input()) for _ in range(5)]
    sero = ''
    for col in range(16):
        for row in range(5):
            try:
                sero += arr[row][col]
            except IndexError:
                continue
    print(f'#{tc} {sero}' )

