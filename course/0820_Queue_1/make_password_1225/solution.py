import sys
sys.stdin = open('input.txt')

'''
숫자 8개를 모두 큐에 넣기
하나씩 디큐하면서 1~5까지 빼기
0보다 크다면 인큐해서 반복
'''


class CQueue:
    def __init__(self, size=10):
        self.front = 0
        self.rear = 0
        self.container = [0] * size
        self.size = size

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def is_empty(self):
        return self.rear == self.front

    def enqueue(self, value):
        if self.is_full():
            print('Q is full')
            raise TypeError('Q is full')
        else:
            self.rear = (self.rear + 1) % self.size
            self.container[self.rear] = value

    def dequeue(self):
        if self.is_empty():
            raise TypeError('Q is empty')
        else:
            self.front = (self.front + 1) % self.size
            return self.container[self.front]


T = 10
for tc in range(1, T+1):
    _ = int(input())
    q = CQueue(8+1)  # front가 빈 칸이어야 함 - 8개의 숫자+1개의 빈칸

    # 숫자를 큐에 넣기
    for item in map(int, input().split()):
        q.enqueue(item)

    is_finished = False  # 모든 연산이 종료되었는지 확인
    while not is_finished:
        # 디큐 후 1~5까지 빼면서
        # 해당 값이 0 초과면 인큐
        # 해당 값이 0 이하면 값을 0으로 하고 인큐 종료
        for i in range(1, 6):
            temp = q.dequeue()
            temp -= i
            if temp > 0:
                q.enqueue(temp)
            else:
                q.enqueue(0)
                is_finished = True
                break

    print(f'#{tc}', end=' ')
    for _ in range(8):
        print(q.dequeue(), end=' ')
    print()