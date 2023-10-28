N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
info.sort(key=lambda x : (x[1],x[0]))
# N이 10만이나 되니 정렬하기는 글렀겠지만 해야하네?
# 거기다 [1]기준으로만 정렬하면 안되는 거였네
cnt = 0
end = 0
for i in range(N):
    if info[i][0] >= end:
        end = info[i][1]
        cnt += 1
print(cnt)