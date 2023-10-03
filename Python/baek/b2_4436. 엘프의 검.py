# Bronze II 4436
# 엘프의 검

while True:
    # EOF 처리
    try:
        n = int(input())
    except:
        break

    lst = [0] * 10
    check = False
    k = 0
    while not check:
        k += 1
        cnt = 0
        for i in str(k * n):
            lst[int(i)] += 1
        for j in lst:
            if j != 0:
                cnt += 1
        if cnt == 10:
            check = True
    print(k)
