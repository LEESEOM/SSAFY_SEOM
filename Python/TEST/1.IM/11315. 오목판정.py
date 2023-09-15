# sw 11315 오목판정
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXaSUPYqPYMDFASQ&categoryId=AXaSUPYqPYMDFASQ&categoryType=CODE&problemTitle=11315&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    cnt = 0
    is_five = 'NO'
    # 가로
    for row in range(N):
        for col in range(N):
            if is_five == 'YES':
                break
            if arr[row][col] == 'o':
                cc = col
                cnt = 1
                while 0 <= cc + 1 < N:
                    cc += 1
                    if arr[row][cc] == 'o':
                        cnt += 1
                        if cnt >= 5:
                            is_five = 'YES'
                            break
                    else:
                        break
    # 세로
    for col in range(N):
        for row in range(N):
            if is_five == 'YES':
                break
            if arr[row][col] == 'o':
                cr = row
                cnt = 1
                while 0 <= cr+1 < N:
                    cr += 1
                    if arr[cr][col] == 'o':
                        cnt += 1
                        if cnt >= 5:
                            is_five = 'YES'
                            break
                    else:
                        break
    # 대각 /
    for row in range(N):
        for col in range(N):
            if is_five == 'YES':
                break
            if arr[row][col] == 'o':
                cr = row
                cc = col
                cnt = 1
                while 0 <= cr + 1 < N and 0 <= cc - 1 < N:
                    cr += 1
                    cc -= 1
                    if arr[cr][cc] == 'o':
                        cnt += 1
                        if cnt == 5:
                            is_five = 'YES'
                            break
                    else:
                        break
    # 대각 \
    for row in range(N):
        for col in range(N):
            if is_five == 'YES':
                break
            if arr[row][col] == 'o':
                cr = row
                cc = col
                cnt = 1
                while 0 <= cr + 1 < N and 0 <= cc + 1 < N:
                    cr += 1
                    cc += 1
                    if arr[cr][cc] == 'o':
                        cnt += 1
                        if cnt == 5:
                            is_five = 'YES'
                            break
                    else:
                        break
    print(f'#{tc} {is_five}')