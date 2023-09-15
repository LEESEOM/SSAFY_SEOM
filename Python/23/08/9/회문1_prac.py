# txt = 'ABCCBA'
# M = len(txt)
# # is_find = True
# is_find = False
# for i in range(M//2):  # 0번부터 M//2 - 1
#     if txt[i] != txt[M-1-i]:
#         # is_find = False
#         break
# else:  # for else > 반복문에서 break 가 수행되지 않으면 / 다른게 없었으면
#     is_find = True

######################################################################
# 길이가 N인 문자열 안에서 길이가 M인 회문이 있는지 검사
txt = 'ABABCCBACB'
N = len(txt)
M = 6
cnt = 0
is_find = False
for i in range(N-M+1):
    #  i : 회문인지 검사하려는 문자열의 시작점
    for j in range(M//2):
        if txt[i+j] != txt[i+M-1-j]:
            break
    else:
        is_find = True
    if is_find:
        print('회문있대!')
        cnt += 1

print(cnt)