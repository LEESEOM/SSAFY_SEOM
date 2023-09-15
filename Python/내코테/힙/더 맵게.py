import heapq

def solution(sco, k):
    global cnt
    cnt = 0
    heapq.heapify(sco)
    while sco[0] < k:
        a = heapq.heappop(sco)
        b = heapq.heappop(sco)
        mix = a+b*2
        heapq.heappush(sco,mix)
        cnt+=1
        if len(sco) == 1 and sco[0] < k:
            cnt = -1
            break
    return cnt

k = 10000
sco = [1,1,1,1,1,1]
cnt = 0
solution(sco,k)
print(cnt)
