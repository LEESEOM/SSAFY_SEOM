my_set = ['A', 'B', 'C']
bit = [0,0,0]
# bit 의 각 요소에다 0과 1을 모두 넣어보기
# bit 의 0번에 0과 1을 넣어준다
for a in range(2):
    bit[0] = a
    for b in range(2):
        bit[1] = b
        for c in range(2):
            bit[2] = c
            for i in range(len(bit)):
                if bit[i]:
                    print(my_set[i], end=' ')
            print()
