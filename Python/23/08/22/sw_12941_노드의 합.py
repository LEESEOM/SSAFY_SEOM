# sw 12941 노드의 합

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for _ in range(M):
        I, J = map(int,input().split())
        tree[I] = J
    # 위로 올리면서 계산하기
    for i in range(N-M,0,-1):
        tree[i] += tree[i*2]
        try:
            tree[i] += tree[i * 2 + 1]
        except IndexError:
            continue
    print(f'#{tc} {tree[L]}')