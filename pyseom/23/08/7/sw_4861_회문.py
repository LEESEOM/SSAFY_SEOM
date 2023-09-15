# sw_4861
def find_palindrome():
    for i in range(N):
        for j in range(N - M + 1):  # j 회문검사 시작점
            # (최대)회문의 길이 절반만큼 검사]
            for k in range(M // 2):
                if data[i][j + k] != data[i][j + M - k - 1]:
                    break  # 계속 확인하는 것보다 아닐 때 중지시키는 게 편함
            else:  # for 문에서 break 가 한번도 수행되지 않으면 실행
                result = []
                for k in range(j, j+M):
                    result.append(data[i][k])
                return ''.join(result)
    for i in range(N):
        for j in range(N - M + 1):  # j 회문검사 시작점
            # (최대)회문의 길이 절반만큼 검사]
            for k in range(M // 2):
                if data[j+k][i] != data[j+M-k-1][i]:
                    break  # 계속 확인하는 것보다 아닐 때 중지시키는 게 편함
            else:  # for 문에서 break 가 한번도 수행되지 않으면 실행
                result = []
                for k in range(j, j+M):
                    result.append(data[k][i])
                return ''.join(result)
    return[]  # 실행 안되는데 넣어주면 예쁘대요


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    result = find_palindrome()
    print(f'#{tc} {result}')

    # N * N 행렬에서
    # 일단 각 행에 회문이 있는지 검사


    # arr = [list(input()) for _ in range(N)]
    # ans = []
    # cnt = 0
    # for i in range(N-M+1):
    #     for j in range(N-M+1):                 # 전체 돌면서
    #         for m in range(M//2):               # M의 반만큼 돌면서
    #             if arr[i][j+m] == arr[i][j+M-m-1]:     # 앞뒤 비교해서 같으면
    #                 ans.append(arr[i][j])         # 아니 일단 리스트에 추가하고
    #                 cnt += 1                       # 같은 횟수가
    #         if cnt == M//2:                         # 전부 같으면
    #             print(ans)                           # 회문이겠죠
    #             break                                 # 이건 가로였고
    #         else:                                      # 아니라면
    #             cnt = 0                                 # 전부
    #             ans = []                                 # 초기화
    #
    #         for n in range(M//2):             # 세로도 마찬가지
    #             if arr[j][i+n] == arr[j+M-n-1][i]:
    #                 ans.append(arr[j][i])
    #                 cnt += 1
    #         if cnt == M:
    #             print(ans)
    #             break
    #         else:
    #             cnt = 0
    #             ans = []