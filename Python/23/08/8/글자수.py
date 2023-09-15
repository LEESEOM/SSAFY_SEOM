# sw 12592. 4865. [파이썬 S/W 문제해결 기본] 3일차 - 글자수

T = int(input())
for tc in range(1, T+1):
    N = input()
    M = input()
    max_cnt = 0
    for i in range(len(N)): # N을 돌면서
        cnt = 0
        for j in range(len(M)): # M 을 돌면서
            if N[i] == M[j]:   # N[i]가 M[j]와 같을 때마다 카운트 +1
                cnt += 1
        if cnt > max_cnt:    # 최대값 구해서 출력
            max_cnt = cnt
    print(f'#{tc} {max_cnt}')
