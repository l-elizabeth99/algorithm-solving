import sys
sys.stdin = open('input.txt')
from collections import deque


def solve_passwords(num):
    q = deque(num)

    is_done = False
    while not is_done:
        for i in range(1, 6):
            passwords = q.popleft() - i
            if passwords <= 0:
                q.append(0)
                is_done = True
                break
            else:
                q.append(passwords)
    return q


T = 10
for tc in range(1, T+1):
    tc_num = int(input())
    data = list(map(int, input().split()))
    print(f'#{tc}', *solve_passwords(data))