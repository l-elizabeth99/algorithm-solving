import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
  A, B, C = map(int, input().split())  # 캔디 정보
  eat_candy = 0  # 먹어야 하는 캔디 수

  # C가 B 이하면 먹어야 하는 캔디 수 계산 및 B 개수 지정
  if C <= B:
    eat_candy += (B - (C - 1))
    B = C - 1

  # B가 A 이하면 먹어야 하는 캔디 수 계산 및 A 개수 지정
  if B <= A:
    eat_candy += (A - (B - 1))
    A = B - 1

  # A, B, C 중 하나라도 0 이하면 -1을 출력
  if A <= 0 or B <= 0 or C <= 0:
    print(f'#{tc}', -1)

  # A, B, C 모두 1개 이상이면 먹어야 하는 캔디 수 출력
  else:
    print(f'#{tc}', eat_candy)