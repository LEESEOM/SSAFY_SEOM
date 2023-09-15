N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
lst = []
for i in range(N):
    a = (((abs(info[i][0])**2)+(abs(info[i][1])**2))**(1/2))/info[i][2]
    lst.append([a,i+1])
lst.sort()
for j in range(N):
    print(lst[j][1])