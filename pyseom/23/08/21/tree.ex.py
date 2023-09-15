# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

V = int(input()) # 정점 수 = 마지막 정점 번호
E = V-1 # tree 의 간선 수 = 정점 수 -1
arr = list(map(int, input().split()))
# 부모를 인덱스로 자식을 저장
ch1 = [0]* (V+1)
ch2 = [0]* (V+1)
for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0: # 자식 1이 아직 없으면
        ch1[p] = c
    else:
        ch2[p] = c

print(ch1)
print(ch2)