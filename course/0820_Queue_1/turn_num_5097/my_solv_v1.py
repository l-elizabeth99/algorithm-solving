import sys
sys.stdin = open('5097_input.txt')

from collections import deque

'''
테스트 케이스를 순회하며
    숫자의 개수와 반복 횟수, 숫자들의 정보를 입력받기
    deque를 지정
    반복 횟수만큼 q의 처음 값을 빼내 제일 뒤로 넣기 반복
    q의 처음 값 출력
'''

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    q = deque(num)
    for _ in range(M):
        q.append(q.popleft())
    print(f'#{tc}', q[0])