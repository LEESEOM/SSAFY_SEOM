# sw 1244 최대 상금

T = int(input())
for tc in range(1,T+1):
    nums, trade = map(int, input().split())
    nums = list(map(int,list(str(nums))))
    ans = []
    while trade:
        if not nums:
            break
        # minnum = 10
        # minidx = 0
        maxnum = 0
        maxidx = 0
        for j in range(len(nums)):
            if nums[j] >= maxnum:
                maxnum = nums[j]
                maxidx = j
            # if nums[j] < minnum:
            #     minnum = nums[j]
            #     minidx = j
        for k in range(len(nums)):
            if trade:
                if maxnum >= nums[k]:
                    nums[k], nums[maxidx] = nums[maxidx], nums[k]
                    trade -=1
                    while max(nums) == nums[0]:
                        ans.append(nums.pop(0))
                        if not nums:
                            break
                break
    nums.sort(reverse=True)
    for m in range(tra):
        ans.append(nums.pop())
    for i in range(len(nums)):
        ans.append(nums[i])
    for i in range(len(nums)):
        ans.append(nums[i])
    print(f"#{tc} {''.join(map(str, ans))}")

#5 88832
#10 987645T