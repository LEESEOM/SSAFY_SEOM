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

    # 이미 선택한 번호를 저장할 집합
    selected_numbers = set()

    # 선택된 값들의 합을 저장할 변수
    total_value = 0

    # 리스트 a와 b에서 번호가 중복되지 않게 값을 선택하면서 합을 최대화
    for val, num in a + b:
        if num not in selected_numbers:
            total_value += val
            selected_numbers.add(num)
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




    # 다 끝나면 총 충전량 출력
    print(f'#{tc} {charge_sum}')
