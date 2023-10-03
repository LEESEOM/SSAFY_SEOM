# Bronze III 26040
# 특정 대문자를 소문자로 바꾸기

C = str(input())
lst = list(map(str, input().split()))
ans = []
for i in C:
    if i in lst:
        ans.append(i.lower())
    else:
        ans.append(i)
print(''.join(ans))