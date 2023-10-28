from collections import deque

N, K = map(int, input().split())
A = max(N, K)
dp = [100000]*(A*2+1)
# K가 더 작을수도 있다는 걸 고려해야 함
dp[N] = 0
deq = deque()
deq.append((N,0))
while deq:
    now, cnt = deq.popleft()
    # 조건 더 줄일 수 있나
    if 0 <= now-1:
        if dp[now-1] > cnt+1:
            dp[now-1] = cnt+1
            deq.append((now-1, cnt+1))
    if now + 1 <= K:
        if dp[now+1] > cnt+1:
            dp[now+1] = cnt+1
            deq.append((now+1,cnt+1))
    if now * 2 < K*2:
        if dp[now*2] > cnt+1:
            dp[now*2] = cnt+1
            deq.append((now*2, cnt+1))
# print(dp)
print(dp[K])