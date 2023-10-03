# s4 2670 연속부분최대곱

N = int(input())
lst = list(float(input()) for _ in range(N))
for i in range(1,N):
    lst[i] = max(lst[i],lst[i]*lst[i-1])
print('%0.3f'%max(lst))
# print(f'{max(lst):.3f}')
# print('{:.3f}'.format(max(lst)))

# print(round(max(lst),3) 은 왜틀림?