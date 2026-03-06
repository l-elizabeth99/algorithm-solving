import sys
sys.stdin = open('re_sample_input.txt')


def find_min_dist():
    total_squared_dist = 0  # 총 거리의 제곱값
    visited = [0] * N  # 방문 기록
    squared_dists = [float('inf')] * N  # 거리의 제곱값을 담을 리스트
    squared_dists[0] = 0  # 시작점 거리는 0
    cnt = 0  # 방문 횟수

    # 섬 개수가 될 때까지 반복
    while cnt < N:
        # 현재 거리의 제곱값과 현재 노드 초기화
        curr_squared_dist = float('inf')
        curr_node = -1

        for prev_node in range(N):
            # 이전 노드를 방문했다면 다음으로
            if visited[prev_node]:
                continue

            # 이전 거리의 제곱값이 현재 거리의 제곱값보다 크면 다음으로
            if squared_dists[prev_node] >= curr_squared_dist:
                continue

            # 현재 거리의 제곱값을 이전 거리의 제곱값으로, 현재 노드를 이전 노드로 갱신
            curr_squared_dist = squared_dists[prev_node]
            curr_node = prev_node

        # 이전 노드를 다 확인했는데도 현재 노드가 갱신되지 않았다면 종료
        if curr_node == -1:
            break

        # 현재 노드 방문처리 후 총 거리의 제곱값에 현재 거리의 제곱값 누적 및 방문 횟수 증가
        visited[curr_node] = 1
        total_squared_dist += curr_squared_dist
        cnt += 1

        for next_node in range(N):
            # 다음 노드를 방문했다면 다음으로
            if visited[next_node]:
                continue

            # 새 거리의 제곱값 계산
            new_squared_dist = (X[next_node] - X[curr_node]) ** 2 + (Y[next_node] - Y[curr_node]) ** 2

            # 다음 거리의 제곱값이 새 거리의 제곱값보다 크다면 다음 거리의 제곱값을 새 거리의 제곱값으로 갱신
            if squared_dists[next_node] > new_squared_dist:
                squared_dists[next_node] = new_squared_dist

    # 총 거리의 제곱값 반환
    return total_squared_dist


T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 섬 개수
    X = list(map(int, input().split()))  # x 좌표
    Y = list(map(int, input().split()))  # y 좌표
    E = float(input())  # 환경 부담 세율 실수

    # 함수 호출 및 환경 부담금 계산 후 결과 출력
    squared_L = find_min_dist()
    result = E * squared_L
    print(f'#{tc} {result:.0f}')