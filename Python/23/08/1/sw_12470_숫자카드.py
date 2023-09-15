# 12470 숫자 카드

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))
    many_cnt = 0
    many_num = 0
    cnt_arr = [0] * 10
    for i in range(N):
        cnt_arr[arr[i]] += 1
    for j in range(10):
        if cnt_arr[j] >= many_cnt:
            many_cnt = cnt_arr[j]
            many_num = j
    print(f'#{tc} {many_num} {many_cnt}')
