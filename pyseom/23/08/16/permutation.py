# perm_arr[idx]에 들어갈 수 있는 애들 다 넣어보기
def perm(idx):
    if idx == N:
        print(perm_arr)
        return

    for i in range(N):
        # 앞에서 쓴 건 넣지 말자
        if used[i] == 0:
            perm_arr[idx] = arr[i]
            used[i] = 1
            perm(idx + 1, used)
            used[i] = 0

def perm2(idx):
    for i in range(idx):
        

arr = [1, 2, 3]
N = 3
perm_arr = [0] * N
used
perm(0, used)