T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(K)]
    # 세로, 가로, 미생물, 방향
    # 상1 하2 좌3 우4

    maps = [[None]+[0]*(N-2)+[None] for _ in range(N-2) ]
    maps.insert(0,[None]*N)
    maps.append([None]*N)
    # M = 시간
    # 자리 넣기

    # 시간 동안

        # 이동한번씩 하기

        # 약품셀 도착하면 바꾸기

        # 겹치면 비교하고 합치기

    # 돌면서 총 마리수 세기