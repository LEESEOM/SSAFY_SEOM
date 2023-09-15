from pprint import pprint

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]




    # 처음에 만나는 줄 저장해두고
    # 아래로 같으면 싹 다 0으로 바꿔버리기 (끝나면 0 한칸은 최소한 띄워져 있음)
    # 근데 이러면 중간에 0있으면 안되니까 좌우도 0인지 비교해서 구분? 중간에
