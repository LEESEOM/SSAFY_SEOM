A, a, B, b, P = map(int,input().split())
if A>P or B>P:
    print('No')
elif B<= a:
    print('Yes')
elif A<=b:
    print('Yes')
elif A+B <= P:
    print('Yes')
else:
    print('No')