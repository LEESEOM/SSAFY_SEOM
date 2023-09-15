# sw 12938 subtree


# 역할 : v를 루트로 하는 서브트리의 노드의 개수 반환
def solve(v):
    # 왼쪽 서브트리 노드 개수 + 오른쪽 서브트리 노드 개수 + 1
    if v == 0:  # 노드가 아닙니다
        return 0
    return solve(tree[0][v])+ solve(tree[1][v]) + 1

T = int(input())
for tc in range(1, T+1):
    E, N = map(int,input().split())
    data = list(map(int, input().split()))
    V = E + 1
    tree = [[0]*(V+1) for _ in range(2)]
    for i in range(0, E*2, 2):
        parent, child = data[i], data[i+1]
        if tree[0][parent] == 0:
            tree[0][parent] = child
        else:
            tree[1][parent] = child
    # print(tree)
    # 트리 N번부터 순회하기
    # 순회방법 : 전 중 후 (사실 dfs)
    # 트리는 일종의 그래프이므로 bfs dfs도 가능
    result = solve(N)
    print(f'#{tc} {result}')



# # my
# T = int(input())
# for tc in range(1, T+1):
#     E, N = map(int,input().split())
#     arr = [[0]*(E+2) for _ in range(E+2)]
#     visited = [0]*(E+2)
#     lst = list(map(int,input().split()))
#     for i in range(E):
#         p = lst.pop(0)
#         c = lst.pop(0)
#         arr[p][c] += 1
#     stack = [N]
#     cnt = 1
#     while stack:
#         t = stack.pop(0)
#         for j in range(E+2):
#             if arr[t][j] == 1 and visited[j] == 0:
#                 stack.append(j)
#                 visited[j] = 1
#                 cnt += 1
#     print(f'#{tc} {cnt}')

