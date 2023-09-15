import heapq


def solution(k, score_lst):
    global result
    heap = []
    result = []
    for i in range(len(score_lst)):
        if len(heap) < k:
            heapq.heappush(heap, score_lst[i])
            result.append(heap[0])
        else:
            if score_lst[i] > heap[0]:
                heapq.heappush(heap, score_lst[i])
                heapq.heappop(heap)
                result.append(heap[0])
            else:
                result.append(heap[0])
    return result

# k = 3
# score = [10,100,20,150,1,100,200]
k = 4
score = [0,300,40,300,20,70,150,50,500,1000]
result = []
solution(score)
print(result)
