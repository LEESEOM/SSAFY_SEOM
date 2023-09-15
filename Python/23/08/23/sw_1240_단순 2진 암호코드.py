# sw 1240 단순 2진 암호코드

# 입력에서 암호코드 찾기
# 이루는 숫자 찾기
# 정상인지 판단
# 결과 출력

password = {'0001101' : 0, '0011001' : 1, '0010011' : 2, '0111101' : 3, '0100011' : 4, \
            '0110001' : 5, '0101111' : 6, '0111011' : 7, '0110111' : 8, '0001011' : 9}
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    code = []
    real = []
    is_find = False
    # 56자리 찾기
    for row in range(N-1,-1,-1):
        if is_find:
            break
        for col in range(M-1,-1,-1):
            if arr[row][col] == '1':
                end = col
                for i in range(end-55, end+1):
                    code.append(arr[row][i])
                is_find = True
                break
    # 숫자 8개로 만들기
    for j in range(0,len(code),7):
        a = ''.join(code[j:j+7])
        real.append(password[a])
    # 규칙 확인
    is_right = True
    cnt1 = 0
    cnt2 = 0
    for k in range(8):
        if k%2 == 0:
            cnt1 += real[k]
        else:
            cnt2 += real[k]
    if ((cnt1*3)+cnt2)%10 != 0:
        is_right = False
    if is_right:
        print(f'#{tc} {cnt1+cnt2}')
    else:
        print(f'#{tc} 0')
