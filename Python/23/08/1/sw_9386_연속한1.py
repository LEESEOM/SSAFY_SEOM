# sw 9386
# 연속한 1의 개수
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input()))   
    max_len = 0                    # 최대 길이
    cnt = 0                        # 연속으로 나올 때 쓸 카운트 변수
    for i in range(N):             # 수열 돌면서
        if arr[i] == 1:            # 1이면 
            cnt += 1               # 카운트 올리고
            if cnt > max_len:      # 지금 저장된 최대값과 비교해서
                max_len = cnt      # 크면 변경
        else:                      # 0이 나오면
            cnt = 0                # 초기화
    print(f'#{tc} {max_len}')
        

 