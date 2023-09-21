import math

N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
run = True
# 일단 교수님이랑 성규 자리 찾기
for row in range(N):
    for col in range(N):
        if info[row][col] == 5:
            a, b = row, col
        elif info[row][col] == 2:
            c, d = row, col
# 거리 5 이상
if math.sqrt(((a - c)**2)+((b - d)**2)) < 5:
    run = False
# 같은 행, 열이면 선분 상 3명
if a==c or b==d:
    if abs(a-c) < 5 and abs(b-d) < 5:
        run = False
# 아니면 직사각형 내 3명
else:
    cnt = 0
    for row in range():
        for col in range():
           if info[row][col] == 1:


if run:
    print('1')
else:
    print('0')