def power_set(idx):
    if idx == N:    # 모든 요소에 대해서 부분집합 포함여부를 결정한 상황
        for i in range(N):
            if selected[i]:
                print(a[i], end=' ')
        print()
        return

    # idx번째 요소를 부분집합에 포함시키거나
    selected[idx] = 1
    power_set(idx+1)
    # idx번째 요소를 부분집합에 포함시키지 않거나
    selected[idx] = 0
    power_set(idx + 1)


a = ['A', 'B', 'C']
N = len(a)
selected = [0] * N  # 각 요소의 부분집합 여부를 표시할 배열열

power_set(0)