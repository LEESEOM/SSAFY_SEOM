T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    min_idx = 0
    max_idx = 0
    for i in range(1, N):
        if arr[min_idx] > arr[i]:
            min_idx = i
        if arr[max_idx] <= arr[i]:
            max_idx = i
    ans = 0
    if max_idx > min_idx:
        ans = max_idx - min_idx
    if min_idx > max_idx:
        ans = min_idx - max_idx
    print(f'#{tc} {ans}')