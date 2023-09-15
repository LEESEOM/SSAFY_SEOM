# 조망권 구하기
# i 번째 건물의 조망권 구하기
# i-1, i-1, i+1, i+2에 있는 건물의 최고 높이 = B
# i 번째 건물의 높이 : A
# 조망권이 있는 세대수 : A - B (단, A > B 이어야 한다)
# 2 <= i <= N-3

for i in range(0, 10):                        # 테스트케이스 여러 번 받기
    N = int(input())
    cnt = 0
    height = list(map(int, input().split()))  # 건물의 높이들 받기
    for j in range(2, N - 2):                 # 건물의 층 중에
        A = height[j]
        B_lst = [height[j - 2], height[j - 1], height[j + 1], height[j + 2]]
        B = 0
        for k in B_lst:
            if k > B:
                B = k
        if A - B > 0:                         # 조망권이 있다면
            cnt += A - B
            B = 0
    print(f'#{i} {cnt}')

 
# max_v = 0                     2칸 이내 건물 중 가장 높은 건물의 높이 구하기
# for j in range(i-2, i+3):
#     if k == i:
#         continue
#     if data[j] > max_v:
#         max_v = data[j]

# cnt = data[i] - max_v if data[i] > max_v else 0
