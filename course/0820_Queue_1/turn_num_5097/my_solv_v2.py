import sys
sys.stdin = open('5097_input.txt')

from collections import deque


def rotate_arr(num):
    q = deque(num)
    for _ in range(M):
        q.append(q.popleft())
    return q[0]


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    n = list(map(int, input().split()))

    print(f'#{tc}', rotate_arr(n))