N, K = map(int, input().split())
stuff = [list(map(int, input().split())) for _ in range(N)]
stuff.sort()
dp = [0]*K+1

