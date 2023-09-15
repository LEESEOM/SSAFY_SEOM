# sw 4047 영준이의 카드 카운팅 (feat. 조현제(토템 : 디버깅 성공 확률 증가))
card = {'S':0, 'D':1, 'H':2, 'C':3}  # 카드 정보
T = int(input())
for tc in range(1, T+1):
    need = [13,13,13,13]    # 필요한 카드 수 담을 리스트
    have = input()    # 받은 카드

    # 3자리씩 나누어서 리스트에 넣기
    lst = []
    for i in range(0, len(have), 3): # 전체를 3자리씩 끊어서
        lst.append(have[i:i+3]) # 3씩 슬라이싱해서 넣기
    # print(lst)  ## ['S01', 'D02', 'H03', 'H04']

    # 중복 확인
    is_error = False
    if len(lst) != len(set(lst)):  # 리스트와 set(리스트)의 길이가 다르다면
        print(f'#{tc} ERROR')      # 중복이 있다는 뜻이므로 에러 출력
        is_error = True
    else:
        for j in range(len(lst)):
            need[card[lst[j][0]]] -= 1  # lst[j][0]은 S D H C 중 하나
                                        # card[ ] 에 넣어서 0,1,2,3 찾아서
    # 출력                              # need[ ] 를 1씩 빼줌
    if not is_error:
        print(f'#{tc}', *need)


    #
    #     num = int(have[i + 1] + have[i + 2])
    #
    #     have[i]
    #
    #
    #
    # S = [0]*13
    # D = [0]*13
    # H = [0]*13
    # C = [0]*13
    # have = list(input())
    # for i in range(0,len(have),3):
    #     num = int(have[i+1]+have[i+2])
    #     if have[i] == 'S':
    #         S[num-1] += 1
    #     if have[i] == 'D':
    #         D[num-1] += 1
    #     if have[i] == 'H':
    #         H[num-1] += 1
    #     if have[i] == 'C':
    #         C[num-1] += 1
    # Scnt = 0
    # Dcnt = 0
    # Hcnt = 0
    # Ccnt = 0
    # is_error = False
    # for k in S:
    #     if k > 1:
    #         is_error = True
    #         break
    #     if k == 0:
    #         Scnt += 1
    # for k in D:
    #     if k > 1:
    #         is_error = True
    #         break
    #     if k == 0:
    #         Dcnt += 1
    # for k in H:
    #     if k > 1:
    #         is_error = True
    #         break
    #     if k == 0:
    #         Hcnt += 1
    # for k in C:
    #     if k > 1:
    #         is_error = True
    #         break
    #     if k == 0:
    #         Ccnt += 1
    # if is_error:
    #     print(f'#{tc} ERROR')
    # else:
    #     print(f'#{tc} {Scnt} {Dcnt} {Hcnt} {Ccnt}')