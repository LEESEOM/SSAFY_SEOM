for tc in range(1,11):
    M = int(input())
    data = [input() for _ in range(8)]
    cnt = 0

    for r in range(8):
        for i in range(8 - M + 1):
            #  i : 회문인지 검사하려는 문자열의 시작점
            is_find = False
            for j in range(M // 2):
                if data[r][i + j] != data[r][i + M - 1 - j]:
                    break
            else:
                is_find = True
            if is_find:
                cnt += 1
            is_find = False
            for j in range(M // 2):
                if data[i + j][r] != data[i + M - 1 - j][r]:
                    break
            else:
                is_find = True
            if is_find:
                cnt += 1
    print(f'#{tc} {cnt}')

