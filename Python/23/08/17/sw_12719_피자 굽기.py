# sw_12719_피자 굽기
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

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))
    # piznum = [1]
    # while 피자가 2개 이상인 동안, Ci에서 0이 아닌 게 1개일 때 까지:
    #     만약 화덕에 자리가 있는데(큐가 다 안 찼는데):
    #         기다리는 피자가 있다면:
    #             넣기
    #             continue
    #     check = front.pop(0)//2
    #     if check == 0:   # 앞쪽 거를 팝해서 모드한게 0이면(다 타버렸으면)
    #         새 피자 투입            # 버리고 새로운 제물을 바친다
    #     else:
    #         append(check)        # 아직 죽지 않았다면 한바퀴 더 돌려버린다
    queue = []
    for i in range(N):
        queue.append(Ci[i],i)  # i를 하나 더 해서 어떤 피자인지 구별

    # 화덕에 있는 핏자 확인하기
    # 다음에 어떤 피자가 들어가야 하는지 알려주는 변수
    next = N
    while True: # len(queue) > 1:
        if len(queue) == 1:
            break
    # 화덕에 제일 먼저 넣은 피자의 양 확인
        cheese, num = queue.pop(0)
        cheese //= 2
        if cheese > 0:  # 다시 돌아가!
            queue.append((cheese, num))
        else:
            if next < M:   # 아직 피자가 있으면
                queue.append((Ci[next],next))
                next += 1
    last = queue.pop(0)
    print(f'#{tc} {last[1+1]}')



