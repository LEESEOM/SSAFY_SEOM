# 12497 D2
# 2일차 - 색칠하기

T = int(input())                            # 테스트 케이스 개수 받기

for tc in range(1, T+1):                    # 테스트 케이스 돌기
    N = int(input())                        # 영역개수 N 받기
    arr = [[0] * 10 for _ in range(10)]     # 10*10의 배열 생성
    purple = 0                              # 보라색인 부분
    info = [list(map(int, input().split())) for _ in range(N)]
    for p in range(0, N):                              # N번 만큼 색칠함
        # r1, c1 ,r2, c2, color = info[i] 해서 언패킹하고 그 값 넣는게 보기 깔끔함
        for i in range(info[p][0], info[p][2]+1):      # 가로 정보 가져옴
            for j in range(info[p][1], info[p][3]+1):  # 세로 정보 가져옴
                arr[i][j] += info[p][4]                # 색 정보 가져와서 해당 위치에 값 더해주기
    for m in range(0, 10):                  # 배열 전체
        for n in range(0, 10):              # 돌면서
            if arr[m][n] == 3:              # 값이 3이라면(빨1+파2)
                purple += 1                 # 보라색 카운트 +1
    print(f'#{tc} {purple}')                # 총 보라색 출력