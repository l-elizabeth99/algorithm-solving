import sys
sys.stdin = open('5201_input.txt')

'''
N개의 컨테이너
M개의 트럭
A->B로 편도로 이동
컨테이너를 트럭에 실음 - 트럭의 적재용량 내에서만 싣기 가능
최대한 많은 무게의 컨테이너를 옮겨야 함
'''

T = int(input())
for tc in range(1, T+1):
  N, M = map(int, input().split())
  w_lst = sorted(map(int, input().split()))  # sorted 반환 값 = list
  t_lst = sorted(map(int, input().split()))

  total = 0

  while w_lst and t_lst:  # 컨테이너와 트럭이 남아있으면 계속 반복
    if w_lst[-1] <= t_lst[-1]:  # 컨테이너 무게가 트럭 적재 중량 이하면
      total += w_lst.pop()
      t_lst.pop()
    else:
      w_lst.pop()  # 컨테이너가 무거워 실을 수 없는 경우

  print(f'#{tc}', total)