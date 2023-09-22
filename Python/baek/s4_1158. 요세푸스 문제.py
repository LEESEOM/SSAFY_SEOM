# s4 1158 요세푸스 문제

N, K = map(int, input().split())
lst = [x for x in range(1,N+1)]
ans = []
now = 0
while lst:
    now += K-1
    if now >= len(lst):
        now = now%len(lst)
    ans.append(str(lst.pop(now)))
print('<', end='')
print(', '.join(ans),end='')
print('>')


