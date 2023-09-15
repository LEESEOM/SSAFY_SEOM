N = int(input())
lst = list(map(int, input().split()))
cnt = 0
for i in range(N):
    is_so = True
    if lst[i] > 1:
        for j in range(2,lst[i]-1):
            if lst[i]%j == 0:
                is_so = False
        if is_so:
            cnt += 1
print(cnt)