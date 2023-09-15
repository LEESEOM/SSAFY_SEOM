# sw 12628 종이붙이기

# f(N) = f(N-2)*2 + f(N-1)

def solve(N):
    if N == 20:
        return 3
    elif N == 10:
        return 1
    return solve(N-20)*2 + solve(N-10)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = solve(N)
    print(f'#{tc} {result}')


def solve1(N):
    N = N//10
    counts = [0] * 31
    counts[1] = 1
    counts[2] = 3
    for i in range(3, N+1):
        count[i] = counts[i-2]*2 + counts[i-1]