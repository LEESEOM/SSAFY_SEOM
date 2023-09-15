# 5
# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25


T = int(input())

arr = [list(map(int, input().split())) for _ in range(T)]

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

result = 0
for i in range(T):       # 행
    for j in range(T):   # 열
        nk = arr[i][j]   # nk-47
        for d in range(4):  # 여기저기
            ni = i + di[d]  # 종
            nj = j + dj[d]  # 황
            if 0 <= ni < T and 0 <= nj < T:
                cnt = abs(arr[ni][nj]-nk)
                result += cnt
print(result)
