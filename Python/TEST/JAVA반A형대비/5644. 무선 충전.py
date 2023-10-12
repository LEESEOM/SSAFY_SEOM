T = int(input())
for tc in range(1, T+1):
    M, A = map(int, input().split())
    # 방향
    d = [[0, 0], [0, -1], [1, 0], [0, 1], [-1, 0]]
    # A 이동 정보
    movea = list(map(int, input().split()))
    # A 초기 위치
    rowa, cola = 1, 1
    # B 이동 정보
    moveb = list(map(int, input().split()))
    # B 초기 위치
    rowb, colb = 10, 10

    # arr[몇번째][0~3]
    # 0 = x, 1 = y, 2 = c, 3 = p
    arr = [list(map(int, input().split())) for _ in range(A)]

    charge_sum = 0

    for i in range(M+1):
        # 주어진 공식 이용해서 판단
        # A와 B가 충전 가능한 곳들을 담을 리스트
        charge_a = []
        charge_b = []
        # 충전소 갯수만큼 돌면서
        for j in range(A):
            # 범위 안이라면 리스트에 추가
            if abs(rowa - arr[j][0]) + abs(cola - arr[j][1]) <= arr[j][2]:
                charge_a.append((arr[j][3], j))
            if abs(rowb - arr[j][0]) + abs(colb - arr[j][1]) <= arr[j][2]:
                charge_b.append((arr[j][3], j))
        # 어차피 둘이니까 숫자로 해도 좋을 것 같긴 한데 튜플로 넣어서 구분
        # 숫자 정렬해서 우선순위도 넣고
        charge_a.sort(reverse=True)
        charge_b.sort(reverse=True)


        # 1번 먼저 선택하는 경우
        temp1, used = 0, -1
        for P, idx in charge_a:
            used = idx
            temp1 += P
            break
        for P, idx in charge_b:
            if used != idx:
                temp1 += P
                break

        # 2번 먼저 선택하는 경우
        temp2, used = 0, -1
        for P, idx in charge_b:
            used = idx
            temp2 += P
            break
        for P, idx in charge_a:
            if used != idx:
                temp2 += P
                break

        # 둘 중에 더 큰 경우 추가
        charge_sum += max(temp1, temp2)

        # 마지막이면 끝냄
        if i == M:
            break

        # 평소에 쓰는 row,col이 아니었음 애초에 반대로 정의해둠
        # 이동
        rowa += d[movea[i]][0]
        cola += d[movea[i]][1]
        rowb += d[moveb[i]][0]
        colb += d[moveb[i]][1]

    # 다 끝나면 총 충전량 출력
    print(f'#{tc} {charge_sum}')
