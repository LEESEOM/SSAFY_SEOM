N, M = map(int, input().split())
known = []
know = list(map(int, input().split()))
for i in range(1, know[0]+1):
    known.append(know[i])
# 체크용으로 앞에 0 넣어두고
party = [[0] + list(map(int, input().split())) for _ in range(M)]
# 순서대로 할 게 아니네
# 진실을 알게 될 파티는 전부 1로 바꾸고
while known:
    a = known.pop()
    for j in range(M):
        if party[j][0] == 0:
            temp = []
            know = False
            for k in range(2, party[j][1]+2):
                if a == party[j][k]:
                    know = True
                else:
                    temp.append(party[j][k])
            if know:
                party[j][0] = 1
                known.extend(temp)

# 마지막에 0갯수 세기
cnt = 0
for i in range(M):
    if party[i][0] == 0:
        cnt += 1
print(cnt)
