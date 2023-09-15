arr = [
    [1,  2,  3,  4,  5],
    [6,  7,  8,  9,  10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]


i, j = 2, 3
# 상(-1,0) 우(0,1) 하(1,0) 좌(0,-1)
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
# for d in range(4):   # d는 방향 : 0 위 1 우 2 하 3 좌
#     ni = i + di[d]
#     nj = j + dj[d]
#     print(arr[ni][nj])

K = 2
N = 5
for d in range(4):
    for a in range(1, K+1):
        ni = i + di[d] * a
        nj = j + dj[d] * a
        if 0 <= ni < N and 0 <= nj < N:  # 범위 안에 있을때만 출력
            print(arr[ni][nj])