# sw 1225 암호생성기

for tc in range(1, 11):
    T = int(input())
    data = list(map(int, input().split()))

    while data[-1] != 0:
        for i in range(1, 6):
            data.append(data.pop(0)-i)
            if data[-1] <= 0:
                data[-1] = 0
                break
    print(f'#{tc}', *data)