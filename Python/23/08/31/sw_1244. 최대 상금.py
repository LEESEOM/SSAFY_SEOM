# # sw 1244 최대 상금
#
# T = int(input())
# for tc in range(1,T+1):
#     nums, trade = map(int, input().split())
#     nums = list(map(int,list(str(nums))))
#     ans = []
#     while trade:
#         if not nums:
#             break
#         maxnum = 0
#         maxidx = 0
#         for j in range(len(nums)):
#             if nums[j] >= maxnum:
#                 maxnum = nums[j]
#                 maxidx = j
#         for k in range(len(nums)):
#             if trade:
#                 if maxnum >= nums[k]:
#                     nums[k], nums[maxidx] = nums[maxidx], nums[k]
#                         ans.append(nums.pop(0))
#                         trade -= 1
#                         if len(nums) == 2 and trade == 1:
#                             break
#                         elif not nums:
#                             break
#                 break
#     for i in range(len(nums)):
#         ans.append(nums[i])
#     print(f"#{tc} {''.join(map(str, ans))}")

#
#5 88832
#10 987645
