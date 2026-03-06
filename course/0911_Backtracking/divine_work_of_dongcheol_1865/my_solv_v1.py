import sys
sys.stdin = open('input.txt')


def find_max_probability(employee_idx, curr_probability):
    global max_probability

    # 가지치기: 현재 확률이 최대 확률 이하면 종료
    if curr_probability <= max_probability:
        return

    # 종료 조건: 모든 직원이 일을 배분받으면 최대 확률을 갱신 후 종료
    if employee_idx == N:
        if curr_probability > max_probability:
            max_probability = curr_probability
        return

    # 모든 직원을 순회
    for idx in range(N):
        # 해당 일이 배분되지 않았다면
        if visited[idx] == 0:
            # 방문 처리 후 재귀 호출한 후 백트래킹
            visited[idx] = 1
            find_max_probability(employee_idx+1, curr_probability*(P_lst[employee_idx][idx]/100))
            visited[idx] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    P_lst = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N  # 방문 기록
    max_probability = 0  # 최대 확률 초기화
    find_max_probability(0, 1.0)  # 초기 확률을 1.0으로 지정
    print(f'#{tc} {max_probability*100:.6f}')  # 결과를 백분율로 출력