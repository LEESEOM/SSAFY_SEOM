N, X = map(int, input().split())
lst = list(map(int, input().split()))
for i in range(len(lst)):
    if lst[i] < X:
        print(lst[i], end=' ')