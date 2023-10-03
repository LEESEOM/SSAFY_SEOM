# S5 16208 귀찮음

# from collections import deque
#
#
# n = int(input())
# deq = deque(list(map(int,input().split())))
# cnt = 1
# cost = 0
# for i in range(n):
#     if n == 1:
#         break
#     if deq[0] < deq[-1]:
#         a = deq.popleft()
#         b = sum(deq)
#         cost += a*b
#     else:
#         a = deq.pop()
#         b = sum(deq)
#         cost += a*b
# print(cost)

#느림

n = int(input())
lst = list(map(int, input().split()))
cost = 0
lst.sort(reverse=True)
le = sum(lst)
for i in range(n):
    if n == 1:
        break
    a = lst.pop()
    le -= a
    cost += a*le
print(cost)
