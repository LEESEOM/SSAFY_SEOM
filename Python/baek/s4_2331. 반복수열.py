# s4 2331 반복수열

A, P = map(int, input().split())
check = [A]
while True:
    tmp = 0
    for i in str(check[-1]):
        tmp += int(i) ** P
    if tmp in check:
        break
    check.append(tmp)

print(check.index(tmp))
