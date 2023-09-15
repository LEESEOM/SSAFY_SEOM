N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
ans = 0
for i in range(N):
    mb = B.index(max(B))
    b = B.pop(mb)
    ans += A[i]*b
print(ans)