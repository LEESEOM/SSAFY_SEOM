# s5 1789 수들의 합

S = int(input())
sumy = 0
i = 1
while sumy <= S:
    sumy += i
    i += 1
print(i-2)
