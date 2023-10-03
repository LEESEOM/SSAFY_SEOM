R = int(input())
SG = list(input())
N = int(input())
FR = [list(input()) for _ in range(N)]
score = 0
max_score = 0
# 먼저 그냥 점수
for i in range(R):                   # 라운드 돌면서
    for j in range(N):               # 친구들 체크하면서
        if SG[i] == 'S':
            if FR[j][i] == 'S':
                score += 1
            elif FR[j][i] == 'R':
                continue
            else:
                score += 2
        elif SG[i] == 'R':
            if FR[j][i] == 'S':
                score += 2
            elif FR[j][i] == 'R':
                score += 1
            else:
                continue
        else:
            if FR[j][i] == 'S':
                continue
            elif FR[j][i] == 'R':
                score += 2
            else:
                score += 1
# 얻을 수 있는 최대 점수
for i in range(R):                   # 라운드 돌면서
    max_r = 0                        # 각 라운드 최대 점수
    cnts = 0                         # 가위, 바위, 보일 때 따로 체크
    cntr = 0
    cntp = 0
    for j in range(N):               # 친구들 체크하면서
        for k in range(3):           # 가위바위보 각각의 기댓값
            if k == 0:
                if FR[j][i] == 'S':
                    cnts += 1
                elif FR[j][i] == 'R':
                    continue
                else:
                    cnts += 2
            elif k == 1:
                if FR[j][i] == 'S':
                    cntr += 2
                elif FR[j][i] == 'R':
                    cntr += 1
                else:
                    continue
            else:
                if FR[j][i] == 'S':
                    continue
                elif FR[j][i] == 'R':
                    cntp += 2
                else:
                    cntp += 1
    max_r += max(cnts, cntr, cntp)
    max_score += max_r

print(score)
print(max_score)