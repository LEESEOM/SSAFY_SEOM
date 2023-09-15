# 카운팅 정렬
N = 10
K = 10
arr = [2, 5, 1, 2, 3, 4, 6, 9, 10, 4]
count = [0] * (K + 1)  # K번 인덱스까지 사용해야 하기 때문임
# 1. 각 요소가 몇번씩 나왔는지 세기
for i in range(N):
    count[arr[i]] += 1
# 2. 카운팅배열 만들기 (누적합) for 각 요소가 들어갈 위치계산
for i in range(1, K + 1):
    count[i] = count[i-1] + count[i]
    # count[i] += count[i - 1]
# 3. 위치에 맞게 알려주기
sorted_arr = [0] * N
for i in range(N - 1, -1, -1):
    # arr[i]이 들어갈 위치
    count[arr[i]] -= 1

    sorted_arr[count[arr[i]]] = arr[i]
print(sorted_arr)
