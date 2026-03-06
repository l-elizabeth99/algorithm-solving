'''
문제 읽기
사탕을 담은 상자
  - A, B, C개
  - 순증가 (A < B < C)
  - 각 상자는 1개 이상

목표
  - 순증가로 만들기 위해 0개 이상 먹기

A상자 - B보다 작게
B상자 - C보다 작게
C상자 - 그대로 두기
'''

'''
설계
1. 완전 탐색
  - B를 C보다 작을 때까지 하나씩 먹기
  - A를 B보다 작을 때까지 하나씩 먹기
  -> 이중 for문으로 구현시 9,000,000번 정도의 연산 발생
    - 최악의 케이스(3,000, 3,000, 3)
    
2. 규칙 세우기
  - B = C - 1 | A = B - 1로 만들면 됨
'''


import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
  # 3개는 따로 받기
  A, B, C = map(int, input().split())

  # 불가능한 케이스 먼저 지우기
  if A < 1 or B < 2 or C < 3:
    print(f'#{tc}', -1)
    continue

  eat_cnt = 0

  # B상자 = C상자 - 1 (B가 C 이상일 때만)
  if B >= C:
    eat_cnt += B - (C-1)
    B = C - 1

  # A상자 = B상자 - 1 (A가 B 이상일 때만)
  if A >= B:
    eat_cnt += A - (B-1)
    A = B - 1

  print(f'#{tc}', eat_cnt)