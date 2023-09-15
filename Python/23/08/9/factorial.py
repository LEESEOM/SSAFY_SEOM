# def fac(N):
#     if N == 0:
#         return 1
#     result = fac(N - 1) * N
#     return result
#
# print(fac(5))

N = 5
bit = [0] * N
def subset(idx):
    for i in range(2):
        bit[idx] = i
        # 여기서는 i가 선택된 상황
        subset(idx+1)