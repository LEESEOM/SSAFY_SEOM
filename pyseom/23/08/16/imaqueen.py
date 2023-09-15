# 한 행에 하나의 퀸을 놓아보기
# 만약 모든 행에 퀸을 다 놓았다면 N개의 퀸을 놓으거니 해를 찾음!
# N * N

N = 4
cnt = 0
def solve(row):
    global cnt
    if row == N:  # 모든 행에 퀸을 놓음
        print('찾음!')
        cnt += 1
        return
    # row 행 모든 열에 퀸 놓아보기
    for col in range(N):
        # row, col 에 놓을 수 있으면 퀸 놓기
        solve(row+1)


