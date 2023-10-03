# dfs로 재귀돌려서 해보면 되지 않을까?
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 20001

    # 어떤 조합으로 나누었을 때 맛의 값을 구하는 공식

