# sw 3499 퍼펙트 셔플

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    deck = list(map(str, input().split()))
    ans = []
    while len(ans) != len(deck):
        for i in range((len(deck)+1)//2):
                ans.append(deck[i])
                if i+((len(deck)+1)//2) <= N-1:
                    ans.append(deck[i+((len(deck)+1)//2)])
    print(f'#{tc}',*ans)

