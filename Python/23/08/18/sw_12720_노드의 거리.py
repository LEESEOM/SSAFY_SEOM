# sw_12720_노드의 거리

T =int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split())
    info = [[0]*(V+1) for _ in range(V+1)]
    visited = [0]*(V+1)
    queue = []
    for i in range(E):
        a, b = map(int, input().split())
        info[a][b] = info[b][a] = 1
    S, G = map(int, input().split())


    visited[S] = 1
    queue.append(S)
    cnt = 1
    for j in range(1, V):           # 거리
        for m in range(cnt):        # 같은 거리 다 돌고나서 j를 갱신되게
            if m == 0:
                cnt = 0
            for k in range(1, V+1): # 다른 숫자들
                if info[queue[0]][k] == 1 and visited[k] == 0:  # 연결되고 안감
                    queue.append(k) # 스택에 넣고
                    cnt += 1        # 카운트 +1
                    visited[k] += j # 거리 값을 visited에 저장
                else:
                    continue
            queue.pop(0)
    print(f'#{tc} {visited[G]}')
