import heapq

def solution(n, works):
    answer = 0
    max_heap = []
    for m in range(len(works)):
        heapq.heappush(max_heap, (-works[m],works[m]))
    for i in range(n):
        a, b = heapq.heappop(max_heap)
        if b == 0:
            heapq.heappush(max_heap, (a, b))
        else:
            heapq.heappush(max_heap, (a+1, b-1))
    for _ in range(len(max_heap)):
        a, b = heapq.heappop(max_heap)
        answer += b**2
    return answer

n = 3
works = [1,1]
solution(n,works)
# print(answer)