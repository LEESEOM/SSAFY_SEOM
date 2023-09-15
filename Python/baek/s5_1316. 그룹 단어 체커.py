N = int(input())
words = [input() for _ in range(N)]
ans = 0
for i in range(N):
    check = []
    cnt = -1
    is_group = True
    for j in range(len(words[i])):
        if words[i][j] not in check:
            check.append(words[i][j])
            cnt += 1
        else:
            if words[i][j] == check[cnt]:
                continue
            else:
                is_group = False
    if is_group:
        ans +=1
print(ans)

