import sys
sys.stdin = open('input.txt')

'''
stack에 숫자를 push하는데

'''


class Stack:
    def __init__(self, size=10):
        self.top = -1                   # top의 초기값은 -1 왜냐면 요소가 없기 때문
        self.container = [0] * size     # 빈 리스트가 아닌 특정 길이만큼 크기를 만들어 줄 필요가 있음
        self.size = size                # 스택의 크기를 저장

    def push(self, value):
        if self.is_full():
            print('full')
            return
        self.top += 1
        self.container[self.top] = value

    def pop(self):
        if self.is_empty():
            print('empty')
            return
        value = self.container[self.top]
        self.container[self.top] = 0
        self.top -= 1

        return value

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size - 1

    def peek(self):
        if self.is_empty():
            print('empty!!')
            return
        return self.container[self.top]

    def get_password(self):
        return ''.join(self.container[:stack.top+1])


T = 10
for tc in range(1, T+1):
    L, arr = input().split()
    L = int(L)  # 길이를 확인하려면 문자가 아니라 숫자로 형변환해야 함

    stack = Stack(L)  # 최대 길이만큼 스택 생성
    for idx in range(L):
        if stack.is_empty() or stack.peek() != arr[idx]:
            stack.push(arr[idx])
        else:
            stack.pop()

    print(f'#{tc}', stack.get_password())