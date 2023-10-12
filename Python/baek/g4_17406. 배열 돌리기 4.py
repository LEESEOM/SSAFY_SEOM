from itertools import permutations
from copy import deepcopy
def spin(arr,order):
    global min_value
    global info
    for j in range(len(order):
        r, s, c = info[order[i][j]][0], info[order[i][j]][1], info[order[i][j]][2]

    return new_arr


N, M, K = map(int, input().split())
arr_origin = [list(map(int, input().split())) for _ in range(N)]
info = [list(map(int, input().split())) for _ in range(K)]
min_value = -float('inf')

# 회전 연산 순서 경우의 수 구하기
# K가 최대 6이라 permutations 그냥 씀
lst = [x for x in range(K)]
orders = list(permutations(lst ,K))

# 회전시키기 > 함수로 만들기
for i in range(len(orders)):
    order = orders[i]
    arr = deepcopy(arr_origin)
    new_arr = spin(arr, order)
    # 한가지 경우 다 돌았을 때
    # 그 경우의 배열 최소값을 구하고
    value = float('inf')
    for k in range(N):
        cnt = sum(new_arr[k])
        if cnt <= value:
            value = cnt
    # 그게 진짜 최소값보다 작으면 갱신
    if value <= min_value:
        min_value = value
print(min_value)
