# sw 13020 이진수2

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    a = 0
    i = 1
    answer = ''
    while True:
        if i >= 13:
            print(f'#{tc} overflow')
            break
        if a + (1*2**-i) > N:
            i += 1
            answer += '0'
        elif a + (1*2**-i) < N:
            a += 1 * 2 ** -i
            i += 1
            answer += '1'
        elif a + (1*2**-i) == N:
            answer += '1'
            print(f'#{tc} {answer}')
            break