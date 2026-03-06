'''
전선 N개
  - 교차점 발생
  - 몇 개 발생하는지 count
  
교차점 발생 규칙
1. 새로운 선
  - 기존의 시작점보다 높음
  - 기존의 도착점보다 낮음
  
2. 새로운 선
  - 기존의 시작점보다 낮음
  - 기존의 도작점보다 높음

3. 하나의 새로운 선에서 여러 개의 교차점이 발생
  - 기존의 전선이 여러 개인 경우
  
- 완전 탐색
  - 새로운 선이 들어올 때마다 기존의 모든 전선과 비교

- 기존 전선 : N-1개
- 비교 N-1번

-> N이 최악인 경우 1,000
-> 약 500,000번 -> 충분히 가능
'''


import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
  N = int(input())

  # N개의 새로운 선이 추가 (기존 선들과 비교)
  wires = []      # 기존선들을 저장할 리스트
  answer_cnt = 0  # 교차점 수

  for _ in range(N):
    start, end = map(int, input().split())

    # 기존 선들과 비교 (교차점 비교)
    for prev_start, prev_end in wires:
      # # 기존 전선보다 높은 시작점, 낮은 도착점
      if start > prev_start and end < prev_end:
        answer_cnt += 1

      # # 기존 전선보다 낮은 시작점, 높은 도착점
      if start < prev_start and end > prev_end:
        answer_cnt += 1

    # 목록에 추가
    wires.append((start, end))
  print(f'#{tc}', answer_cnt)