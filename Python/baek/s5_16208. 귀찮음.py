# S5 16208 귀찮음

n = int(input())
lst = list(map(int, input().split()))
lst.sort()
le = sum(lst)
cost = 0
for i in range(n):
    le -= lst[i]
    cost += lst[i]*le
print(cost)