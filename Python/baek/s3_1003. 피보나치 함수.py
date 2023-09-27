# s3 1003 피보나치 함수

T = int(input())
for _ in range(T):
    N = int(input())
    zero, one = 1, 0
    for i in range(N):
        zero, one = one, zero+one
    print(zero, one)
