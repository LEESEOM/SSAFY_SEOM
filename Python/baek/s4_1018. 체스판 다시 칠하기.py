# s4 1018 체스판 다시 칠하기

N, M = map(int, input().split())
info = [list(input()) for _ in range(N)]

ans = 32
for row in range(N-7):
    for col in range(M-7):
        cnt = 0
        a = info[row][col]
        x = (row + col) % 2
        for i in range(8):
            for j in range(8):
                y = (row+col+i+j)%2
                b = info[row+i][col+j]
                if x==y and a != b:
                    cnt += 1
                if x!=y and a == b:
                    cnt += 1
        if cnt > 32:
            cnt = 64-cnt
        if cnt < ans:
            ans = cnt
print(ans)
