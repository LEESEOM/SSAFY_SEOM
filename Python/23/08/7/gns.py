T = int(input())
for _ in range(T):
    tc, N = input().split()
    N = int(N)
    data = input().split()
    gns_dict = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
    # 카운팅 정렬 > 요소를 인덱스로 표현 가능해야 사용할 수 있음
    # 최소 최대값이 차이가 많이 나면 비효율적
    # 갯수 세고 누적합 구해서 위치구 하고 자리 넣기
    count = [0] * 10
    sorted_data = [None] * N
    # 갯수 세고(data 순회하면서)
    for i in range(N):
        count[gns_dict[data[i]]] += 1 # 오우
    for i in range(1, 10):
        count[i] = count[i] + count[i-1]
    for i in range(N):
        # data[i]가 어디에 들어갈 지 확인하고 sorted_data 에 넣어주면 됨
        count[gns_dict[data[i]]] -= 1 # 인덱스니까 1은 빼주기
        sorted_data[count[gns_dict[data[i]]]] = data[i]
    print(tc)
    print(*sorted_data)





    # data = 문자열로 이루어진 리스트 > 정렬 불가능
    # data.sort(key=lambda x:gns_dict[x]) << 짱쉬움



    # 선택정렬 - 너무 느리다
    # for i in range(N-1):
    #     # 최소값 찾아서 i 번째에 넣어주기 (자리 바꾸기)
    #     min_idx = i # 비교 대상 중에 제일 앞에 있는 수를 임의로 선택
    #     for j in range(i+1,N):
    #         if gns_dict[data[min_idx]] > gns_dict[data[j]]:
    #             min_idx = j
    #     data[i], data[min_idx] = data[min_idx], data[i]

