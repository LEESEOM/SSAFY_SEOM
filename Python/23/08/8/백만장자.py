# sw 1859. 백만 장자 프로젝트 D2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cost = list(map(int, input().split()))
    benefit = 0  # 이득 값
    max_val = 0
    lst = []
    for i in range(N-1,-1,-1):   # 뒤에서부터
        if cost[i] > max_val:   # 최대값이 바뀐다면
            for j in range(len(lst)):    # lst 를 돌면서
                if not lst:
                    continue
                benefit += (max_val - lst[j])  # 기존 최대가격 기준으로 이득 정산
            lst = []                           # 리스트 초기화
            max_val = cost[i]                  # 최대가격 갱신
        lst.append(cost[i])                    # 리스트에 넣어줌
        if i == 0:                             # 끝까지 왔으면
            for k in range(len(lst)):
                benefit += (max_val - lst[k])  # 현재 최대 가격 기준으로 정산
    print(f'#{tc} {benefit}')



    # 리스트에 넣는 방식도 모자람
    # lst = []
    # for i in range(N):
    #     lst.append(cost[i])        # 현재 값을 리스트에 올림
    #     for j in range(len(lst)):
    #         if cost[i] > lst[j]:              # i가 lst 의 요소보다 크다면
    #             benefit += cost[i] - lst[j]   # i - lst 값을 benefit 에 더하고
    #             lst[j] = cost[i]              # 해당 요소를 i로 바꿈
    # print(f'#{tc} {benefit}')






    # while indexing 하면 시간 터져요
    # max_idx = cost.index(max(cost))
    # while True:
    #     max_idx = cost.index(max(cost))      # 할당, 갱신
    #     if max_idx == 0:                     # 최고 가격의 인덱스가 0이라면
    #         del cost[:max_idx + 1]           # 하나를 더 지워주고
    #         if not cost:                     # 리스트가 비었으면
    #             break                        # 끝
    #         if cost:                         # 남아있으면
    #             continue                     # 계속
    #     for i in range(max_idx):   =          # 최대값 인덱스 기준으로 이전 친구들
    #         benefit += max(cost) - cost[i]   # 이득에 차이만큼 더함
    #     del cost[:max_idx]                   # 앞쪽 배열 지워버리고
    # print(f'#{tc} {benefit}')



    # 최고 가격 기준으로 앞에 있는 걸 다 팔고
    # 최고 가격이 배열 중간에 있다면
    # 그 이후에서 또 다시 최고 가격을 찾아서 반복

    # while 에서 인덱싱해서 망한듯
    # 그렇다면 최대값을 찾고 범위만 새로 지정하여 max 사용하지 않고 그때그때 찾기