# 힙만들어서 삽입하는 연산
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
# heap 역할을 할 완전 이진 트리를 배열로 만들기
heap = [0]*100
# 어느 위치에 요소가 들어가야 하는지 알려주는 변수
heap_pointer = 1
heap_push(7)
heap_push(5)
heap_push(2)
heap_push(3)
heap_push(4)
heap_push(6)



print(heap)