# s2 1927 최소 힙

import sys
import heapq

heap = []
N = int(input())
for i in range(N):
    a = int(sys.stdin.readline())
    if a == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap,a)