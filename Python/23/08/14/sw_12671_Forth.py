# sw 12671 Forth

T = int(input())
for tc in range(1, T + 1):
    code = input().split()
    stack = []
    op = ['+', '-', '*', '/']
    for i in range(len(code)):
        if i not in op:
            stack.append(i)
        if i in op:
            if i == '+':

            if i == '-':

            if i == '*':

            if i == '/':

