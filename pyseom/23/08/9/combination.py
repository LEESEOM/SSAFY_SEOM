# 조합 : (1,2,3,4,5) 중에서 3개 골라라
# 5C3
arr = [1,2,3,4,5]
N = 5
M = 3
selected = [0] * N
def comb(idx, cnt):
    if cnt == M:  # 원하는 개수만큼 요소를 선택함
        print(selected)
        return
    if idx == N:  # 끝까지 갔는데도 cnt 못채움
        return
    for i in range(2):
        selected[idx] = i
        comb(idx+1, cnt+i)
        selected[idx] = 0
    # selected[idx] = 0
    # comb(idx+1, cnt)
    # selected[idx] = 1
    # comb(idx+1, cnt+1)

comb(0,0)