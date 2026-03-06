import sys
sys.stdin = open('5209_input.txt')


def find_min_cost(factory_idx, curr_cost):
    global min_cost

    # 가지치기: 현재 비용이 최소 비용 이상이면 종료
    if curr_cost >= min_cost:
        return

    # 종료 조건: 모든 공장이 제품을 생산하면 최소 비용 갱신 후 종료
    if factory_idx == N:
        if curr_cost < min_cost:
            min_cost = curr_cost
        return

    # 모든 공장을 순회
    for idx in range(N):
        # 해당 공장을 사용하지 않았다면
        if visited[idx] == 0:
            # 방문 처리 후 재귀 호출한 후 백트래킹
            visited[idx] = 1
            find_min_cost(factory_idx+1, curr_cost+V[factory_idx][idx])
            visited[idx] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 제품 개수
    V = [list(map(int, input().split())) for _ in range(N)]  # 공장별 생산 비용
    visited = [0] * N  # 방문 기록
    min_cost = float('inf')  # 최소 비용 초기화
    find_min_cost(0, 0)  # 함수 호출
    print(f'#{tc}', min_cost)  # 최소 비용 출력