T = int(input())
for tc in range(1, T+1):
    M, A = map(int, input().split())
    movea = list(map(int, input().split()))
    moveb = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(A)]
    maps = [[0]*10 for _ in range(10)]
    charge_sum = 0

    #이동
    # 일단 시작 지점 충전 가능하면 넣기
    rowa = cola = 1
    rowb = colb = 10
    charge_a = []
    charge_b = []
    for j in range(A):
        D = abs(rowa - arr[j][0]) + abs(cola - arr[j][1])
        D2 = abs(rowb - arr[j][0]) + abs(colb - arr[j][1])
        if D <= arr[j][2]:
            charge_a.append((arr[j][3], j))
        if D2 <= arr[j][2]:
            charge_b.append((arr[j][3], j))
    # 과연 이게 겹치는 경우가 있을까 싶긴 하지만 그래도 나누는 방법 찾아야할듯
    charge_a.sort(reverse=True)
    charge_b.sort(reverse=True)

    for i in range(M):
        # a 이동
        if movea[i]== 1:
            rowa -= 1
        elif movea[i]== 2:
            cola += 1
        elif movea[i]== 3:
            rowa += 1
        elif movea[i]== 4:
            cola -= 1
        # b 이동
        if moveb[i]== 1:
            rowb -= 1
        elif moveb[i]== 2:
            colb += 1
        elif moveb[i]== 3:
            rowb += 1
        elif moveb[i]== 4:
            colb -= 1

        # 주어진 공식 이용해서 거리로 해야할 듯?
        charge_a = []
        charge_b = []
        for j in range(A):
            D = abs(rowa - arr[j][0]) + abs(cola - arr[j][1])
            D2 = abs(rowb - arr[j][0]) + abs(colb - arr[j][1])
            if D <= arr[j][2]:
                charge_a.append((arr[j][3],j))
            if D2 <= arr[j][2]:
                charge_b.append((arr[j][3],j))
        # 어차피 둘이니까 숫자로 해도 좋을 것 같긴 한데 튜플로 넣어서 구분각
        # 숫자 정렬해서 우선순위도 넣고
        charge_a.sort(reverse=True)
        charge_b.sort(reverse=True)

        # 1) 둘 다 2개 이상 있을 때
            # 서로의 두번째로 큰 것을 비교
            # 두번째가 더 큰 쪽에서 가장 큰 걸 선택
            # 반대쪽에서 가장 큰 것과 같은지 비교하고 다르면 그거 같으면 다음거
        # 2) 한 쪽만 2개 이상일 때
            # 2-1) 반대 쪽이 1개일 때
                # 1개인 쪽을 고르고
                # 같지 않은 것 중에 제일 큰 거 고르기
            # 2-2) 반대 쪽이 0개일 때
                # 그냥 제일 큰거 고르기
        # 3) 2개 이상인 쪽이 없을 때
            # 둘다 그냥 고르기


    # 다 끝나면 총 충전량 출력
    print(f'#{tc} {charge_sum}')
