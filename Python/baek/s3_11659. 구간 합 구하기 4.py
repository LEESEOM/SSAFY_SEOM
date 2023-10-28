N, M = map(int, input().split())
numbers = list(map(int, input().split()))
section = [list(map(int, input().split())) for _ in range(M)]
# 다른 리스트에 누적합을 전부 더해놓고 시작점과 끝점의 차이만 계산하기
sum_v = [0]*N
sum_v[0] = numbers[0]
for i in range(1,N):
    sum_v[i] += sum_v[i-1] + numbers[i]
for j in range(M):
    start, end = section[j][0], section[j][1]
    if start == 1:
        print(sum_v[end-1])
    else:
        print(sum_v[end-1]-sum_v[start-2])
# 당연히 시간초과가 나니까 정답률이 이따위겠죠?
# for i in range(M):
#     sum_v = 0
#     start, end = section[i][0], section[i][1]
#     for j in range(start-1, end):
#         sum_v += numbers[j]
#     print(sum_v)