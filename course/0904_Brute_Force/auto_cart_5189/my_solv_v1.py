import sys
sys.stdin = open('5189_input.txt')


# 최솟값 찾는 함수
def find_min_battery(curr_location, visited, current_cost, costs, n):
    global min_battery

    # 종료조건: 모든 구역을 방문 시 종료
    if len(visited) == n:
        # 사무실(0)로 돌아오는 비용 계산, 최솟값 갱신
        total_cost = current_cost + costs[curr_location][0]
        min_battery = min(min_battery, total_cost)
        return

    # 재귀 호출: 방문하지 않은 구역을 탐색
    for next_location in range(n):
        # 다음 위치가 현재 위치이거나, 이미 방문한 구역이면 건너뛰기
        if next_location == curr_location or next_location in visited:
            continue

        # 새로운 경로 상태 기록: 방문한 곳, 비용 갱신
        new_visited = visited + [next_location]
        new_cost = current_cost + costs[curr_location][next_location]

        # 가지치기: 갱신한 비용이 최솟값 이상이면 건너뛰기
        if new_cost >= min_battery:
            continue

        # 재귀 호출: 다음 단계로 넘어가 경로 탐색
        find_min_battery(next_location, new_visited, new_cost, costs, n)


# 풀이 함수
def solve_golf_problem(costs):
    global min_battery
    n = len(costs)  # 배열의 길이를 지정
    visited = [0]  # 방문 기록: 사무실에서 시작
    find_min_battery(0, visited, 0, costs, n)  # 최솟값 찾는 함수 호출

    return min_battery  # 최솟값 반환


# 테스트 케이스 입력
T = int(input())
for t in range(1, T + 1):
    N = int(input())  # 배열 크기
    costs = [list(map(int, input().split())) for _ in range(N)]  # N x N 비용 배열
    min_battery = float('inf')  # 최솟값을 무한대로 지정
    result = solve_golf_problem(costs)  # 풀이 함수 호출 및 결과에 할당
    print(f'#{t}', result)  # 결과 출력