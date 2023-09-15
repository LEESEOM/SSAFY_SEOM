# b2 2798 블랙잭
from itertools import combinations

N, M = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0

for i in combinations(lst,3):
    if ans < sum(i) <= M:
        ans = sum(i)
print(ans)
