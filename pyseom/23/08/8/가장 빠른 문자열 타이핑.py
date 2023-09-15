# sw 3143 .
# 가장 빠른 문자열 타이핑

T = int(input())
for tc in range(1, T+1):
    N, M = input().split()
    check = 0
    cnt = 0
    i = 0
    j = 0
    while True:
        if len(M) == 1:       # M 길이가 1이면 어차피 똑같다
            break
        if N[i] == M[j]:      # 지금 자리가 같다면
            check += 1
        i += 1
        j += 1
        if check == len(M):   # M만큼 연속으로 같았다면 = B가 있었다면
            cnt += 1          # B의 갯수 +1
            check = 0         # 체크 변수 초기화
            j = 0             # j도 초기화
        if i == len(N):       # N을 다 돌았다면 종료
            break
        if N[i] != M[j]:      # 다르다면 j만 초기화 해서 다음 i와 M을 다시 비교시작
            check = 0
            j = 0
    print(f'#{tc} {len(N)-(cnt*(len(M)-1))}')
