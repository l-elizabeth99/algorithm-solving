import sys
sys.stdin = open('input.txt')

'''
행을 먼저 순회하며 모든 정수를 순회
상하좌우로 움직이며 해당 칸의 수가 현재 칸의 수+1인지 확인 후
맞다면 횟수를 1 증가, 그 칸을 현재 칸으로 두고 재귀 호출 후 이동거리 반환
해당 칸의 정보 리스트에 반환된 횟수와 시작점을 튜플로 넣기
최대 횟수와 비교해 최대 횟수를 갱신하고 그때의 시작점 반환
    - 최대 횟수가 같다면 시작점의 수가 작은 경우를 시작점으로 반환 
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 정수 개수
    A = [list(map(int, input().split())) for _ in range(N)]  # NxN 정수

    print(f'#{tc}')