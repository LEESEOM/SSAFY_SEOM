from collections import deque


def solution(numbers, target):
    answer = 0
    qu = deque()
    qu.append((numbers[0],0))
    qu.append((-numbers[0],0))
    while qu:
        val, i = qu.popleft()
        if i == len(numbers)-1:
            if val == target:
                answer += 1
        else:
            i += 1
            qu.append((val + numbers[i], i))
            qu.append((val - numbers[i], i))
    return answer