# sw 4366 정식이의 은행업무

T = int(input())
for tc in range(1, T+1):
    bi = list(map(str, input()))
    tri = list(map(str, input()))
    same = False
    while not same:
        for i in range(len(bi)):
            if same:
                break
            if bi[i] == '1':
                bi[i] = '0'
            else:
                bi[i] = '1'
            for j in range(len(tri)):
                for k in range(2):
                    if tri[j] == '0':
                        tri[j] = '1'
                    elif tri[j] == '1':
                        tri[j] = '2'
                    else:
                        tri[j] = '0'
                    if int(''.join(bi),2) == int(''.join(tri),3):
                        same = True
                        print(f'#{tc} {int("".join(bi),2)}')
                        break
                if tri[j] == '0':
                    tri[j] = '1'
                elif tri[j] == '1':
                    tri[j] = '2'
                else:
                    tri[j] = '0'
            if bi[i] == '1':
                bi[i] = '0'
            else:
                bi[i] = '1'