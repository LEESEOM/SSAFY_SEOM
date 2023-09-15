# sw 1952 수영장
def dfs(m, cost):
    global min_cost
    if m >= 13:
        if cost < min_cost:
            min_cost = cost
    else:
        dfs(m+1,cost+plan[m])
        dfs(m+3,cost+qurter)

T = int(input())
for tc in range(1, T+1):
    day, month, qurter, year = map(int, input().split())
    plan = [0] + list(map(int, input().split()))
    min_cost = year
    for i in range(13):
        if day * plan[i] >= month:
            plan[i] = month
        else:
            plan[i] = day * plan[i]
    dfs(1,0)
    print(f'#{tc} {min_cost}')