# import math
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     ans = 0
#     ans = math.factorial(M)//(math.factorial(N)*math.factorial(M-N))
#     print(ans)

# 이건 메모리초과
# from itertools import combinations
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     a = [0]*M
#     print(len(list(combinations(a,N))))

import math
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    print(math.comb(M,N))



