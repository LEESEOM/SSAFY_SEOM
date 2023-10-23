from collections import deque

N, M = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]
ans = float('inf')

# 1: 우, 2: 반대, 3: 직각, 4: 삼방, 5: 사방
# 1,3,4 = 4번 다돌리기 / 2 = 1번만 돌리기 / 5 = 안돌려도됨

# cctv 돌리는 조합인데 순서라기보단 1-1~4, 2-1or2 이런 느낌이라 어떻게 할 지 모르겠네

        # 뭔가 순서대로 돌렸다가 손해보면 어쩌으냐
        # 하나씩 다 돌려보면서 예측치를 넣어두기?
    # 5 빼고 돌려보면서 최소화되는 것 찾기
# 5를 미리 돌려둘까
    # 돌리다가 손해면 멈추기?

# 그 조합에서 사각지대 계산
# 체크할 배열 새로 만들어주고
method = []
arr = info[:]
# 방향으로 쭉 바꾸면서 벽만나면 멈추기
for i in range(len(method)):
    cnt = 0
    for j in range(len(method[i])):
        deq = deque()
        while deq:
    # 방향 따라서??
            nr = row
            nc = col
            if 0<=nr<N and 0<=nc<M and arr[nr][nc] != '6':
                arr[nr][nc] = '1'
                #deq.append((nr,nc))
    # 다 끝나면 0 갯수 세고 제일 적으면 갱신
    for row in range(N):
        for col in range(M):
            if arr[row][col] == '0':
                cnt += 1
    if cnt <= ans:
        ans = cnt

print(ans)
