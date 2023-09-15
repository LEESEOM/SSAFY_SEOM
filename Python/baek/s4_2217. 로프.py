N = int(input())
lst = [int(input()) for _ in range(N)]
lst.sort(reverse=True)
ans = []
for i in range(N):
    ans.append(lst[i]*(i+1))
print(max(ans))
