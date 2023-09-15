N, K = map(int, input().split())
lst = [int(input()) for _ in range(N)]
lst.sort(reverse=True)
now = 0
cnt = 0
i = 0
while now < K:
    if now + lst[i] <= K:
        now += lst[i]
        cnt += 1
        if now == K:
            break
    else:
        i += 1
print(cnt)