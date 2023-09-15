# swea 문제풀이 1974. 스도우 검증 풀이

# 같은 줄에 1에서 9까지 숫자를 한번씩만 넣고 3x3크기 생각

def sudoku(arr):
    for i in range(9):
        cnt = [0] * 10
        for j in range(9):
            cnt[arr[i][j]] += 1
        for k in range(1, 10):
            if cnt[k] == 0:     # 0 인 경우
                return 0        # 0 리턴

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    ans = sudoku(arr)
    print(f'{tc} {ans}')

    '''
    ans = 1 # 스도쿠가 완성되면 1, 아니면 0
    이 방법이 있지만 def 함수로 표현해보자
    for i in range(9):
        cnt = [0] * 10
        for j in range(9):
            cnt[arr[i][j]] += 1
        for k in range(1, 10):
            if cnt[k] == 0:     # 0 인 경우
                ans = 0
                break           # for k 에 대해 종료
        if ans == 0:
            break
    '''