T = int(input())
lst = [list(map(str,input())) for _ in range(T)]
for i in range(T):
    stack = []
    is_yes = True
    for j in range(len(lst[i])):
        if lst[i][j] == '(':
            stack.append('(')
        else:
            if stack:
                a = stack.pop()
                if a != '(':
                    is_yes = False
                    break
            else:
                is_yes = False
                break
    if stack:
        is_yes = False
    if is_yes:
        print('YES')
    else:
        print('NO')

