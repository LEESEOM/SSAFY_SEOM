def dfs(idx, num):
    global max_num
    global min_num
    if idx == N-1:
        if num >= max_num:
            max_num = num
        if num <= min_num:
            min_num = num
        return


    for i in range(4):
        if info[i] > 0:
            info[i] -= 1
            if i == 0:
                new = num + nums[idx + 1]
            elif i == 1:
                new = num - nums[idx + 1]
            elif i == 2:
                new = num * nums[idx + 1]
            elif i == 3:
                # 음수 나누기
                new = int(num / nums[idx + 1])
            dfs(idx + 1, new)
            info[i] += 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    info = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    max_num = -100000000
    min_num = 100000000
    dfs(0,nums[0])
    print(f'#{tc} {max_num-min_num}')
