# 중위표기식 > 후위표기식
# 연산 우선 순위가 높은 애가 먼저 출력될 수 있도록 해야 한다.
exp = '(6+5*(2-8)/2'
# N = len(exp)
post_exp = ''
stack = []
# 우선순위를 비교하기 위한 딕셔너리 생성
# 괄호 때문에......괄호 처리를 위해서 우선순위표를 2개 만듭니다.
# stack 안에 있을 때랑 밖에 있을 때랑 우선순위가 달라요 >>> 괄호가
# stack 안에 있을 때:
# 괄호 안에 다른 연산자들 다 처리하고 괄호가 없어져야 하니까 우선순위 낮음
# 스택에 들어가려고 할 때
# 다른 연산자들보다 괄호가 먼저 처리 되어야 한다. 우선순위가 높음
isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}
for c in exp:
    # 하나씩 읽어오기
    # 피연산자 vs 연산자
    # 피연산자라면 출력
    # 연산자라면 우선순위에 따라서 스택에 넣거나 출력
    if c in '+-*/()':  # 연산자
        if c == ')':  # 여는 괄호 만날 때 까지 모조리 pop
            while stack[-1] != '(':
                post_exp += stack.pop()
            stack.pop()    # 여는 괄호는 버리기
            continue    # 다음토큰 읽어오기
        
        if not stack:
            stack.append(c)
        # stack 의 top 의 연산자보다 우선 순위가 높으면 그냥 넣으면 됨
        elif isp[stack[-1]] < icp[c]:
            stack.append(c)
        else:  # 같거나 높으면...일단 스택에 있는 애들 다 뺄 건데
            # 나보다 우선순위가 낮은 애가 스택에 들어있으면 들어가면 됩니다
            # 계속 뺄건데 나보다 낮은 애가 탑이 될 때 까지 뺄 거에요
            while stack and isp[stack[-1]] >= icp[c]:
                post_exp += stack.pop()
            # 나보다 우선순위 높은 애들은 다 출력했으니 push
            stack.append(c)
    else:  # 피연산자
        post_exp += c

while stack:   # 스택에 남아있는 연산자 출력
    post_exp += stack.pop()

print(post_exp)