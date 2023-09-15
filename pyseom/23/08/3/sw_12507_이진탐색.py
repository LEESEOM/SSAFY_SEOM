# sw 12507
# 이진탐색

T = int(input())

for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    cnt_a = 0                           # a와 b 찾는데 걸리는 횟수 세서 비교
    cnt_b = 0
    start = 1                           # 1페이지부터 마지막 페이지까지
    end = P
    while True:
        mid = (start + end)//2
        if mid == Pa:
            break
        if mid > Pa:
            end = mid
        if mid < Pa:
            start =mid
        cnt_a += 1
    start = 1
    end = P
    while True:
        mid = (start + end)//2
        if mid == Pb:
            break
        if mid > Pb:
            end = mid
        if mid < Pb:
            start =mid
        cnt_b += 1
    if cnt_a == cnt_b:
        print(f'#{tc} 0')
    if cnt_a > cnt_b:
        print(f'#{tc} B')
    if cnt_a < cnt_b:
        print(f'#{tc} A')