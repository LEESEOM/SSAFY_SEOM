# 트리만든다음에 후위연산 하시면 됩니다
# 노드가 값 그대로 반환
# 노드가 연산자라면 왼쪽 자식 오른쪽 자식 연산해서 결과를 반환
# v번 노드 연산결과 반환
def post_order(v):
    if type(tree[v][0]) == int:
       return tree[v][0]
    left = post_order(tree[v][1])
    right = post_order(tree[v][2])
    if tree[v][0] == '+':
        return left+right
    elif tree[v][0] == '-':
        return left-right
    elif tree[v][0] == '*':
        return left*right
    else:
        return left//right



for tc in range(1, 11):
    N = int(input())
    tree = [[0]*3 for _ in range(N+1)]
    for _ in range(N):
        node = input().split()  # 얘가 4개 아니면 2개
        # if len(node) == 4:
        if node[1] in '*/+-':
            num = int(node[0])
            # 0번이 노드 번호, 1번이 연산자, 2번이 왼쪽 자식 노드 번호, 3번이 오른쪽 자식 노드 번호
            tree[num][0] = node[1]
            tree[num][1] = int(node[2])
            tree[num][2] = int(node[3])
        else:
            tree[int(node[0])][0] = int(node[1])
    result = post_order(1)
    print(f'#{tc} {result}')