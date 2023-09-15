# sw 18602 문제 제목 붙이기(파이썬)

alpha = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
         'I': 9, 'J': 10, 'K': 11, 'L':12, 'M':13, 'N': 14, 'O': 15, 'P': 16,
         'Q': 17, 'R': 18, 'S': 19, 'T': 20,'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = []
    for _ in range(N):
        lst.append(input())
    cnt = 0
    check = 1
    is_connect = True
    while is_connect:
        is_connect = False
        for i in range(len(lst)):
            if check == alpha[lst[i][0]]:
                cnt += 1
                is_connect = True
                break
        if not is_connect:
            continue
        check += 1
    print(f'#{tc} {cnt}')