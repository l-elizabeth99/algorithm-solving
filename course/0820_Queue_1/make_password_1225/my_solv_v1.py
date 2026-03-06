import sys
sys.stdin = open('input.txt')
from collections import deque

T = 10
for tc in range(1, T+1):
    tc_num = int(input())
    data = list(map(int, input().split()))
    # False 가 될 때까지 반복
    # 순회하며 데이터의 첫 번째 수를 i만큼 빼기 반복
    # 이때 감소한 수가 0보다 작거나 같으면 0으로 저장 -> 즉시 해당 숫자 배열을 암호로 반환
    q = deque(data)

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
    print(f'#{tc}', *q)