# sw 13068 베이비진 게임2
T = int(input())
for tc in range(1, T+1):
    deck = list(map(int, input().split()))
    player1 = []
    player2 = []
    is_draw = True
    is_done = False
    for i in range(0,12,2):
        if not is_done:
            player1.append(deck[i])
            if i > 5:
                check = [0] * 10
                for j in range(len(player1)):
                    check[player1[j]] += 1
                for k in range(10):
                    if check[k] == 3:
                        print(f'#{tc} 1')
                        is_done = True
                        is_draw = False
                        break
                    elif k <= 7:
                        if check[k] >=1 and check[k + 1] >=1 and check[k + 2] >= 1:
                            print(f'#{tc} 1')
                            is_done = True
                            is_draw = False
                            break
            if not is_done:
                player2.append(deck[i+1])
                if i > 5:
                    check = [0] * 10
                    for j in range(len(player2)):
                        check[player2[j]] += 1
                    for k in range(10):
                        if check[k] == 3:
                            print(f'#{tc} 2')
                            is_done = True
                            is_draw = False
                            break
                        elif k <= 7:
                            if check[k] >= 1 and check[k + 1] >= 1 and check[k + 2] >= 1:
                                print(f'#{tc} 2')
                                is_done = True
                                is_draw = False
                                break
        else:
            break
    if is_draw:
        print(f'#{tc} 0')