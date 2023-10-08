T = int(input())
for tc in range(1, T+1):
    M, A = map(int, input().split())

    d = [[0, 0], [0, -1], [1, 0], [0, 1], [-1, 0]]
    movea = list(map(int, input().split()))
    rowa, cola = 1, 1
    moveb = list(map(int, input().split()))
    rowb, colb = 10, 10

    # arr[몇번째][0~3]
    # 0 = x, 1 = y, 2 = c, 3 = p
    arr = [list(map(int, input().split())) for _ in range(A)]

    charge_sum = 0

    for i in range(M+1):
        # 먼저 지금 자리 구하고 나서
        # 주어진 공식 이용해서 거리로 해야할 듯?
        charge_a = []
        charge_b = []
        for j in range(A):
            if abs(rowa - arr[j][0]) + abs(cola - arr[j][1]) <= arr[j][2]:
                charge_a.append((arr[j][3], j))
            if abs(rowb - arr[j][0]) + abs(colb - arr[j][1]) <= arr[j][2]:
                charge_b.append((arr[j][3], j))
        # 어차피 둘이니까 숫자로 해도 좋을 것 같긴 한데 튜플로 넣어서 구분각
        # 숫자 정렬해서 우선순위도 넣고
        charge_a.sort(reverse=True)
        charge_b.sort(reverse=True)

        # 1번 먼저 선택
        temp1, used = 0, -1
        for P, idx in charge_a:
            used = idx
            temp1 += P
            break
        for P, idx in charge_b:
            if used != idx:
                temp1 += P
                break

        # 2번 먼저 선택
        temp2, used = 0, -1
        for P, idx in charge_b:
            used = idx
            temp2 += P
            break
        for P, idx in charge_a:
            if used != idx:
                temp2 += P
                break

        # 큰 경우 추가
        charge_sum += max(temp1, temp2)

        # 마지막이면 끝냄
        if i == M:
            break

        # 반대 아닌가????????????
        # 평소에 쓰는 row,col이 아니었음 애초에 반대로 정의해둠
        # 이동
        rowa += d[movea[i]][0]
        cola += d[movea[i]][1]
        rowb += d[moveb[i]][0]
        colb += d[moveb[i]][1]

    # 다 끝나면 총 충전량 출력
    print(f'#{tc} {charge_sum}')
