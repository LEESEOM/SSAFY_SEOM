# 2007 패턴 마디의 길이

T = int(input())
for tc in range(1, T+1):
    mstr = input()
    madi = mstr[0]
    madi += mstr[1]
    is_find = False
    for i in range(2, 11):
        if is_find:
            break
        if mstr[i+1] == madi[1]:
            if mstr[i] == madi[0]:
                for j in range(2,i):
                    madi += mstr[j]
                    is_find = True
            else:
                continue
    print(f'#{tc} {len(madi)}')
    # 틀림 ㅋㅋ

    # T = int(input())
    # for test_case in range(1, T + 1):
    #     s = input()
    #     for j in range(1, 11):
    #         if s[:j] == s[j:2 * j]:
    #             print(f'#{test_case} {j}')
    #             break