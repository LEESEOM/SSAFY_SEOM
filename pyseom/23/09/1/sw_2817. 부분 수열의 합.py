# sw 2817 부분 수열의 합
def power_set(idx):
    global cnt
    if idx == N:
        sumy = 0
        for i in range(N):
            if selected[i]:
                sumy += nums[i]
        if sumy == K:
            cnt += 1
        return

    selected[idx] = 1
    power_set(idx+1)
    selected[idx] = 0
    power_set(idx + 1)


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    selected = [0] * N
    cnt = 0
    power_set(0)
    print(f'#{tc} {cnt}')
