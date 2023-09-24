from collections import deque

def merge_sort(lst):
    global cnt
    if len(lst) == 1:
        return lst
    left = deque()
    right = deque()
    mid = len(lst)//2
    for x in range(0,mid):
        left.append(lst[x])
    for y in range(mid,len(lst)):
        right.append(lst[y])
    merge_sort(left)
    merge_sort(right)

    return merge(left, right)

def merge(left, right):
    global cnt
    result = deque()
    while left or right:
        if left and right:
            if left[0] <= right[0]:
                result.append(left.popleft())
            else:
                result.append(right.popleft())
        elif left:
            result.append(left.popleft())
            if not left:
                cnt += 1
        elif right:
            result.append(right.popleft())
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    ans = merge_sort(lst)
    print(lst)
    print(ans)
    print(N//2)
    print(f'#{tc} {ans[(N//2)]} {cnt}')

