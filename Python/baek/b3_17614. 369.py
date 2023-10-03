# B3 17614
# 369

T = int(input())

cnt = 0
for num in range(1, T+1):
    for i in str(num):
        if i == '3' or i == '6' or i == '9':
            cnt += 1
print(cnt)
