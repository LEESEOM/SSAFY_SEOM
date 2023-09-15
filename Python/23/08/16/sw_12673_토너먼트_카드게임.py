# sw 12673 토너먼트 카드게임

def solve(start, end):
    # start~end 번의 학생들 중의 승자를 찾기 위해
    m = (start + end) // 2

    w1 = solve(start,m)
    w2 = solve(m+1,end)
    if start ==

    # w1과 w2의 결과를
    # 반환

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = list(map(int, input().split()))
    alive = [0]*N
    solve(N)