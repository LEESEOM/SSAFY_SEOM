# sw 12510
# 특별한 정렬

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ans = []                               # 답을 넣을 리스트
    arr = list(map(int, input().split()))
    while len(ans) != 10:                  # 10개가 들어갈 때까지
        max_num = 0                        # 최대 최소 설정
        min_num = 100
        for i in range(N):                 # 최대 구하기
            if arr[i] > max_num:
                max_num = arr[i]
            if arr[i] < min_num:           # 최소 구하기
                min_num = arr[i]
        ans.extend([max_num, min_num])     # ans 에 max, min 추가하고
        arr.remove(max_num)                # arr 에서는 삭제
        arr.remove(min_num)
        N -= 2                             # arr 에서 삭제되었으니 길이 감소 반영
    print(f'#{tc}',*ans)

