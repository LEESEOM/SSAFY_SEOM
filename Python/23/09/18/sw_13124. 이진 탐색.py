def binarysearch(lst, key):
    global cnt

    low = 0
    high = N-1
    check = 0
    while low <= high:
        mid = (low+high) // 2
        if A[mid] == key:
            cnt += 1
            return
        elif A[mid] > key:
            if check == 1:
                break
            else:
                high = mid - 1
                check = 1
        else:
            if check == 2:
                break
            else:
                low = mid + 1
                check = 2
    return


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for i in range(len(B)):
        key = B[i]
        binarysearch(A, key)
    print(f'#{tc} {cnt}')
