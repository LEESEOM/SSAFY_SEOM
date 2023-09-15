class MyStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.s = [None] * max_size   # max_size : 최대 개수
        self.top = -1  # 요소를 빼거나, 들어갈 위치를 알려주는 변수(마지막 위치)
    # push, pop, is_empty, is_full, peek
    def push(self,data):
        # 요소를 stack 에 삽입
        self.top += 1
        self.s[self.top] = data
    def pop(self):
        # stack 에 들어있는 마지막 요소를 삭제, 반환
        result = self.s[self.top]
        self.top -= 1
        return result
        # 뒤쪽은 접근할 수 없고 어차피 덮어씌워짐
    def is_empty(self):
        if self.top == -1:
            return True
        return False
    def is_full(self):
        if self.top == max_size-1:
            return True
        return False
    # is_empty, full 을 그냥 push pop 의 조건으로 넣어버려도 상관은 없음
    def peek(self):
        if not self.is_empty():
            return self.s[self.top]
# data = input()
# N = len(data)
# stack = MyStack(N)
# is_ok = True
# for i in range(N):
#     # 여는 괄호면 stack 에 push
#     # 닫는 괄호면 stack 에서 pop 해서 짝이 맞는지 검사
#     if data[i] == '(':
#         stack.push(data[i])
#     else:
#         if stack.is_empty():
#             is_ok = False
#             break
#         stack.pop()
# # 모든 반복문을 다 돌았을 때
# if not is_ok or not stack.is_empty():
#     print('응애')
# else:
#     print('굿잡')



# stack = MyStack(10)
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
# stack.push(5)
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())


