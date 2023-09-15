# import itertools
#
# N = list(input())
# ans = []
# lst = list(itertools.permutations(N, len(N)))
#
# for i in range(len(lst)):
#     num = int(''.join(lst[i]))
#     if num%30 == 0:
#         ans.append(num)
# if not ans:
#     print(-1)
# else:
#     print(max(ans))

# N = input()
N = sorted(input(), reverse=True)
cnt = 0
if '0' not in N:
    print(-1)
else:
    for i in range(len(N)):
        cnt += int(N[i])
    if cnt%3 != 0:
        print(-1)
    else:
        print(''.join(N))
