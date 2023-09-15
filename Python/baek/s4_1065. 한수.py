N = input()
ans = 99
for i in range(1,int(N)+1):
    if int(N) < 100:
        ans = int(N)
        break
    else:
        lst = []
        if i > 100:
            for j in range(3):
                lst.append(int(str(i)[j]))
        print(lst)

