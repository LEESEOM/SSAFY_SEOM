T = int(input())

for tc in range(1, T+1):             # 테스트 케이스를 돌면서
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_cs = 0                        # 최대 킬 수는 테스트 케이스마다 초기화
    for i in range(0, N-M+1):         # 각 arr 을 돌면서
        for j in range(0, N-M+1):
            cs = 0                    # 킬 수는 [i][j]마다 초기화
            for m in range(0, M):     # arr[i][j] 일때 [i+m][j+m]까지의 합을 다 더해서
                for n in range(0, M):
                    cs += (arr[i+m][j+n])  # 킬 수에 넣고
            if cs > max_cs:              # 다 더했을 때 최대 킬 수 보다 크다면
                max_cs = cs              # 최대값 갱신
    print(f'#{tc} {max_cs}')             # ij 다 돌고 최대값 출력



