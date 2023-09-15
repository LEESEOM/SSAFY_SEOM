# sw 5432 쇠막대기 자르기

T = int(input())
for tc in range(1,T+1):
    info = list(map(str, input()))
    stick = 0
    jo_gak = 0
    for i in range(len(info)):
        if info[i] == '(':
            stick += 1
        if info[i] == ')':
            if info[i-1] == '(':
                stick -= 1
                jo_gak += stick
            else:
                stick -= 1
                jo_gak += 1
    print(f'#{tc} {jo_gak}')

