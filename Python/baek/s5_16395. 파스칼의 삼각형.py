# S5 16395
# 파스칼의 삼각형

n, k = map(int, input().split())
arr = [[1]]
for i in range(1, n):
    arr.append([0] * (i + 1))
    for j in range(i + 1):
        if j == 0 or j == i:
            arr[i][j] = 1
        else:
            arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]
if n == 1:
    print(1)
else:
    print(arr[i][k - 1])
