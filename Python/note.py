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
            new = int(num / nums[idx + 1])
        dfs(idx + 1, new)
        info[i] += 1

