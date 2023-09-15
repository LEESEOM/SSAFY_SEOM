# Silver V 6417
# 코코넛 그 두 번째 이야기

N = int(input())

while N > 0:  # N이 -1이 들어온다면 종료
    n = N  # N을 나누고 나중에 N 출력해서 값이 바뀌는거 방지
    K = []
    for num in range(2, n + 1):
        for i in range(1, num+1):  # 사람 수 만큼 나누는게 가능한지
            if (n - 1) % num == 0:  # 지금 가능하다면
                n = (n - 1)*(num-1) // num  # 다음번도 가능한지 다시 세팅
                if i == num:  # 전부 나누는데 성공했다면
                    K.append(num)  # 사람 수를 K 리스트에 추가
            else:
                n = N
                break
    if K:  # K가 존재한다면 max(K)출력
        print(f'{N} coconuts, {max(K)} people and 1 monkey')
    else:
        print(f'{N} coconuts, no solution')
    N = int(input())
