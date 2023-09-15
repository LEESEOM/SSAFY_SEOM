# sw 12940 이진 힙

def heap_push(data):
    global heap_pointer
    # 완전 이진트리 형태를 유지하기 위해서
    # 이진트리의 마지막(heap_pointer)에 넣어주고
    heap[heap_pointer] = data
    # 방금 넣은 요소가 heap 조건 만족하는지 확인
    # 아니라면 바꿔주는 것을 반복
    child = heap_pointer
    parent = child//2
    while parent > 0 and heap[child] < heap[parent]:
        # if heap[child] < heap[parent]:
        heap[child], heap[parent] = heap[parent], heap[child]
        # else:
        #     break
        child = parent
        parent = child // 2
    heap_pointer += 1


T = int(input())
for tc in range(1 ,T+1):
    N = int(input())
    heap = [0]*(N+1)
    info = list(map(int, input().split()))
    heap_pointer = 1
    cnt = 0
    for i in range(N):
        heap_push(info[i])
    a = N
    while a != 1:
        a //= 2
        cnt += heap[a]
    print(f'#{tc} {cnt}')