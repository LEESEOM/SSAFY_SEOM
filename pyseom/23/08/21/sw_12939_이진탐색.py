# v : 현재 정점의 번호
def inorder(v):
    global cnt
    if v > N:    # 만약 정점이 최대 정점보다 크면 아무것도 하지마라
        return
    # 중위순회 : 현재정점에서 작업을
    # 왼쪽 서브트리에서 작업 끝나고 오른쪽 서브트리 작업 시작하기 전에
    # 작업하면 됩니다
    inorder(v*2)
    # 현재노드작업 : 적절한 숫자 넣어주기
    tree[v] = cnt
    cnt += 1
    inorder(v * 2 + 1)
    pass

# 크기 N인 완전 이진트리 만들기
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    # how to
    # 완전이진트리는 배열로 만들면 편합니다
    tree = [None]*(N+1)
    # 완전 이진트리를 중위순회 해야 한다.
    cnt = 1
    inorder(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')
