from pprint import pprint

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(K)]
    # 상1 하2 좌3 우4
<<<<<<< HEAD
=======

>>>>>>> 9d698a8d9dae233be9425989eeb910368d286658
    maps = [[None]+[0]*(N-2)+[None] for _ in range(N-2) ]
    maps.insert(0,[None]*N)
    maps.append([None]*N)
    # M = 시간
    # 자리 넣기
    for i in range(K):
        maps[info[i][0]][info[i][1]] = (info[i][2],info[i][3])

    # 시간 동안
    for _ in range(K):
        pass
        # 이동한번씩 하기
        # 약품셀 도착하면 바꾸기(타노스 하고 방향 반대로)

        # 겹치면 비교하고 합치기

    # 돌면서 총 마리수 세기