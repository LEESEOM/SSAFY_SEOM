N, M = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]
ans = float('inf')

# 1: 우, 2: 반대, 3: 직각, 4: 삼방, 5: 사방
# 1,3,4 = 4번 다돌리기 / 2 = 1번만 돌리기 / 5 = 안돌려도됨

# cctv 돌리는 조합

    # 뭔가 순서대로 돌려서 손해를 보면 어쩌으냐
    # 하나씩 다 돌려보면서 예측치를 넣어두기?
    # 5 빼고 돌려보면서 최소화되는 것 찾기


# 그 조합에서 사각지대 계산
arr = info[:]
# 방향으로 쭉 바꾸면서 벽만나면 멈추기

# 다 끝나면 0 갯수 세고 제일 적으면 갱신
cnt = 0
for row in range(N):
    for col in range(M):
        if arr[row][col] == '0':
            cnt += 1
if cnt <= ans:
    ans = cnt


print(ans)
