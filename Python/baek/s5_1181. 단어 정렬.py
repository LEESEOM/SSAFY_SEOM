N = int(input())
lst = [input() for _ in range(N)]
lst.sort()
lst.sort(key=len)
new_lst = []
for i in range(len(lst)):
    if lst[i] not in new_lst:
        new_lst.append(lst[i])
        print(lst[i])