# S5 1769 3의 배수

X = input()
cnt = 0
while len(X) != 1:
    Y = 0
    for i in range(len(X)):
        Y += int(X[i])
    X = str(Y)
    cnt += 1
print(cnt)
if int(X)%3 == 0:
    print('YES')
else:
    print('NO')
