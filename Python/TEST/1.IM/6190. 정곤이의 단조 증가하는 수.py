# sw 6190 정곤이의 단조 증가하는 수

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numlst = list(map(int, input().split()))
    # print(numlst) numlst = [2,4,7,10]
    danjo = []
    for i in range(N-1):
        for j in range(1+i,N):
            dan = str(numlst[i]*numlst[j])
            check = 1
            is_danjo = True
            for k in range(len(dan)):
                if int(dan[k]) < check:
                    is_danjo = False
                else:
                    check = int(dan[k])
            if is_danjo:
                danjo.append(int(dan))

    if not danjo:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {max(danjo)}')