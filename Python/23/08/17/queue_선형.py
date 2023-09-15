class MyQueue2:  # 원형
    def __init__(self, N):
        self.queue = [None] * N
        self.front = self.rear = 0

    def en_queue(self, data):
        #  rear를 1 증가하고 그 위치에 데이터 삽입
        if not self.is_full():
            self.rear = (self.rear + 1) % len(self.queue)
            self.queue[self.rear] = data

    def de_queue(self):
        if not self.is_empty():
            self.front = (self.front + 1) % len(self.queue)
            return self.queue[self.front]

    def is_full(self):
        # rear의 다음 칸이 wfront라면 가득 참
        # front랑 rear가 같은 칸에 있으면 비어있다고 판단하기 때문에
        # front의 위치에 데이터를 삽입하면 안됨
        if (self.rear + 1) % len(self.queue) == self.front:
            return True
        return False

    def is_empty(self):
        if self.front == self.rear:
            return True
        return False
#
#
# class MyQueue:
#
#     def __init__(self, N):
#         self.queue = [None] * N
#         self.front = self.rear = -1
#
#     # queue에 데이터 삽입
#     def en_queue(self, data):
#         if not self.is_full():
#             self.rear += 1
#             self.queue[self.rear] = data
#
#     # queue에 가장 먼저 돌아온 요소를 삭제 및 반환
#     def de_queue(self):
#         if not self.is_empty():
#             self.front += 1
#             return self.queue[self.front]
#
#     def is_full(self):
#         if self.rear == (len(self.queue) - 1):
#             return True
#         return False
#
#     def is_empty(self):
#         if self.rear == self.front:
#             return True
#         return False
#
#
# queue = MyQueue2(10)
# queue.en_queue2(5)
# queue.en_queue2(4)
# queue.en_queue2(3)
# queue.en_queue2(2)
# queue.en_queue2(1)
#
# print(queue.de_queue2())
# print(queue.de_queue2())
# print(queue.de_queue2(2))
# print(queue.de_queue2())
# print(queue.de_queue2())
