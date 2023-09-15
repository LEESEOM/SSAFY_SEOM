# b1 1546 평균

from statistics import mean

N = int(input())
lst = list(map(int, input().split()))
a = max(lst)
ans = []
for i in range(N):
    ans.append((lst[i]/a)*100)
print(mean(ans))