# S4 2422 한윤정이 이탈리아에 가서 아이스크림을 사먹는데

N, M = map(int, input().split())
arr = [[0]*N for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    arr[a-1][b-1] = arr[b-1][a-1] = 1
for i in range(N):
    arr[i][i] = 1
lst = []
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if arr[i][j] == 0 and arr[j][k] == 0 and arr[k][i] == 0:
                lst.append(tuple(sorted([i+1,j+1,k+1])))
print(len(set(lst)))

