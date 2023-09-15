# 그림 그려보니
# (r,c) > (c, N-1-r)

def rotate90(origin):
    new_mat = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            new_mat[c][N-1-r] = origin[r][c]
    return new_mat


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mat = [list(input().split()) for _ in range(N)]
    mat90 = rotate90(mat)
    mat180 = rotate90(mat90)
    mat270 = rotate90(mat180)
    print(f'#{tc}')
    for i in range(N):
        print(''.join(mat90[i]), end=' ')
        print(''.join(mat180[i]), end=' ')
        print(''.join(mat270[i]), end=' ')
        print()