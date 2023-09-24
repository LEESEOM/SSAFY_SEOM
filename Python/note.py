from itertools import permutations

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

# 처음에 0인 녀석들의 (row, col)정보를 따로 저장해 두고
blank = []
for row in range(N):
    for col in range(M):
        if arr[row][col] == 0:
            blank.append((row,col))
lst = list(permutations(blank,3))
for i in range(len(lst)):
    for j in range(3):
        x,y = lst[i][j]
        print(x,y)