import sys
sys.stdin = open('sample_input.txt')


def recur(cnt, subset):
  global count

  # 종료 조건 - 자연수의 개수만큼 반복하면 합을 계산
  if cnt == N:
    curr_sum = sum(subset)
    # 합이 K와 같으면 count 1 증가
    if curr_sum == K:
      count += 1
    return

  # 부분집합에 포함 시키는 경우
  recur(cnt + 1, subset + [A[cnt]])
  # 포함 시키지 않는 경우
  recur(cnt + 1, subset)


T = int(input())
for tc in range(1, T+1):
  N, K = map(int, input().split())  # 자연수의 개수, 합
  A = list(map(int, input().split()))  # N개의 자연수 수열
  A.sort()  # 오름차순으로 수열 정렬
  count = 0  # 합이 K인 부분 수열의 수를 담을 변수
  recur(0, [])  # 함수 호출
  print(f'#{tc}', count)  # 개수 출력