N = int(input())
nums = [list(map(int, input().split()))]
info = [list(map(int, input().split())) for _ in range(N)]
ans = 10*100
# 연결 정보 이중리스트로 받기
arr = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(info[i][0]):
        arr[i][info[i][j+1]-1] = 1

# 가능한 부분집합들 만들기
poss = []

tmp1 = []
tmp2 = []
temp = [(tmp1, tmp2)]


if cnt == 2:
    poss.append(temp)


# bfs로 가다가 연결이 끊기면 되돌아가거나 하는 방법?


# 값들 계산하기
if poss:
    for i in range(len(poss)):
        lst1, lst2 = poss.pop()
        a = abs(sum(lst1) - sum(lst2))
        if a <= ans:
            ans = a
# 최소값 출력(나눌 수 없다면 -1)
if ans == 10*100:
    print(-1)
else:
    print(ans)