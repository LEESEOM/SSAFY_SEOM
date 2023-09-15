# sw 1974 스도쿠 검증
T = int(input())
for tc in range(1, T+1):
    puzzle = [list(map(int, input().split())) for _ in range(9)]
    is_True = True
    for i in range(9):
        cnt = [0] * 10
        for j in range(9):
            cnt[puzzle[i][j]] += 1
        for k in range(1, 10):
            if cnt[k] != 1:
                is_True = False
                break
    for i in range(9):
        cnt = [0] * 10
        for j in range(9):
            cnt[puzzle[j][i]] += 1
        for k in range(1, 10):
            if cnt[k] != 1:
                is_True = False
                break
    # 네모
    for i in range(0,9,3):
        for j in range(0,9,3):
            cnt = [0] * 10
            for m in range(i,i+3):
                for n in range(j,j+3):
                    cnt[puzzle[m][n]] += 1
            for k in range(1, 10):
                if cnt[k] != 1:
                    is_True = False
                    break
    if is_True:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')