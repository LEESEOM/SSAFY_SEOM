dr = [0,0,1,-1]
dc = [1,-1,0,0]

def run(cnt, x, y):
    global max_cnt
    global check
    if cnt > max_cnt:
        max_cnt = cnt
    for i in range(4):
        nr = x + dr[i]
        nc = y + dc[i]
        if 0<=nr<R and 0<=nc<C and not check[ord(board[nr][nc])-65]:
            check[ord(board[nr][nc])-65] += 1
            run(cnt+1,nr,nc)
            check[ord(board[nr][nc])-65] -= 1


R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
check = [0]*26
check[ord(board[0][0])-65] = 1
max_cnt = 0
run(1,0,0)

print(max_cnt)