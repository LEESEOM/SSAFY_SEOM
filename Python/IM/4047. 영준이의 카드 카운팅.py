# sw 4047 영준이의 카드 카운팅 (feat. 조현제(토템 : 디버깅 성공 확률 증가))

T = int(input())
for tc in range(1, T+1):
    S = [0]*13
    D = [0]*13
    H = [0]*13
    C = [0]*13
    have = list(input())
    for i in range(0,len(have),3):
        num = int(have[i+1]+have[i+2])
        if have[i] == 'S':
            S[num-1] += 1
        if have[i] == 'D':
            D[num-1] += 1
        if have[i] == 'H':
            H[num-1] += 1
        if have[i] == 'C':
            C[num-1] += 1
    Scnt = 0
    Dcnt = 0
    Hcnt = 0
    Ccnt = 0
    is_error = False
    for k in S:
        if k > 1:
            is_error = True
            break
        if k == 0:
            Scnt += 1
    for k in D:
        if k > 1:
            is_error = True
            break
        if k == 0:
            Dcnt += 1
    for k in H:
        if k > 1:
            is_error = True
            break
        if k == 0:
            Hcnt += 1
    for k in C:
        if k > 1:
            is_error = True
            break
        if k == 0:
            Ccnt += 1
    if is_error:
        print(f'#{tc} ERROR')
    else:
        print(f'#{tc} {Scnt} {Dcnt} {Hcnt} {Ccnt}')
