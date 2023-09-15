# sw 1289 원재의 메모리 복구하기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV19AcoKI9sCFAZN&categoryId=AV19AcoKI9sCFAZN&categoryType=CODE&problemTitle=1289&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

T = int(input())
for tc in range(1, T+1):
    memo = input()
    cnt = 0
    is_first = True
    now = '0'
    for i in range(len(memo)):
        if memo[i] == '1' and is_first:
            cnt += 1
            is_first = False
            now = '1'
            continue
        elif i >= 1:
            if memo[i] != memo[i-1]:
                cnt += 1
                now = memo[i]
    print(f'#{tc} {cnt}')