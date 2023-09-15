while True:
    a = input()
    if a == '0':
        break
    yes = True
    for i in range(len(a)//2):
        if a[0+i] != a[-1-i]:
            yes = False
    if yes:
        print('yes')
    else:
        print('no')
