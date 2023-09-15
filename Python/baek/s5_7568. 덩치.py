# s5 7568 덩치

N = int(input())
lst = []
for i in range(N):
    a, b = map(int, input().split())
    lst.append((a,b))
ans = []
for i in range(N):
    cnt = 1
    for j in range(N):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            cnt += 1
    ans.append(cnt)
print(*ans)

