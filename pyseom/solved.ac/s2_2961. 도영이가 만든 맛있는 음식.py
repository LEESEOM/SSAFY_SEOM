from itertools import combinations
import math

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
result = []
for i in range(len(lst)+1):
    result = result+list(combinations(lst,i))
result.pop(0)
ans = 9999999999
for j in range(len(result)):
    sin = 1
    sun = 0
    for k in range(len(result[j])):
        sin *= result[j][k][0]
        sun += result[j][k][1]
        a = abs(sin-sun)
        if a <= ans:
            ans = a
print(ans)
