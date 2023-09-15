# sw 1954
# 달팽이 숫자

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    dx = [0, 1, 0, -1]               # 방향정보 리스트
    dy = [1, 0, -1, 0]
    arr = [[0]*N for _ in range(N)]  # 0으로 이루어진 N*N 배열 생성
    cnt = 1  # 올려가면서 배열에 넣어줄 값
    m = 0    # 이동, 방향 전환 시 참고할 dx,dy 인덱스값
    x, y = 0, 0  # 현재 위치 arr[x][y]에 쓰일 좌표값
    while cnt != N**2+1:  # cnt 가 N**2가 되면 (= 모든 칸을 다 돌면) 끝
        arr[x][y] = cnt  # 현재 위치에 cnt 값 넣기
        try:
            if arr[x+dx[m]][y+dy[m]] != 0:  # 다음 칸이 0이 아니라면 (이미 지나온 칸이라면)
                m = (m+1)%4  # 방향 전환 - 인덱스 값을 1 올려줌 (3일때도 (3+1)%4이므로 0으로 돌아가면서 순환)
        except IndexError:  # 벽이라서 인덱스 에러 뜨는거 예외처리
            m = (m + 1) % 4
        x, y = (x+dx[m]), (y+dy[m])  # 이동
        cnt += 1
    print(f'#{tc}')
    for i in range(N):
         print(' '.join(map(str, arr[i])))