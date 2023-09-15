# 문자열 뒤집기

# 중간 값을 찾아서 좌우 변경
# 0 <-> N - 1
# 1 <-> N - 2
# 2 <-> N - 3

# range(N//2)

data = 'Reverse this string'
data = list(data)
N = len(data)
its_true = True
for i in range(N//2):

    # print(data[i],end=' ')
    # i 번은 N-1-i 번이랑 자리를 바꾸면 됩니다
    # data[i], data[N-1-i] = data[N-1-i], data[i]

    # 문자열 뒤집기
    # if data[i] != data[N-1-i]:
    #     return False
print(''.join(data))
