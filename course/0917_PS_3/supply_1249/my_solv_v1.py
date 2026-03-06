import sys
sys.stdin = open('input.txt')

from heapq import heappop, heappush


def find_min_recovery_time():
    # 델타값
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    recovery_times = [[float('inf')] * N for _ in range(N)]  # 최소 복구 시간를 담을 경로
    recovery_times[0][0] = 0  # 시작점 초기화
    pq = [(0, 0, 0)]  # 시작점 (현재까지의 복구 시간, y, x)

    # pq가 빌 때까지 반복
    while pq:
        # pq에서 뺀 값 지정
        curr_recovery_time, curr_y, curr_x = heappop(pq)

        # 상하좌우만큼 반복하며 다음 좌표값 지정
        for k in range(4):
            ny = curr_y + dy[k]
            nx = curr_x + dx[k]

            # 유효하지 않으면 종료
            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue

            # 새로운 최소 복구 시간 계산
            new_recovery_time = curr_recovery_time + map_lst[ny][nx]

            # 현재 복구 시간이 새로운 복구 시간보다 작으면 종료
            if recovery_times[ny][nx] <= new_recovery_time:
                continue

            # 현재 복구 시간을 새로운 복구 시간으로 갱신 및 pq에 새로운 복구 시간과 새 좌표값 넣기
            recovery_times[ny][nx] = new_recovery_time
            heappush(pq, (new_recovery_time, ny, nx))

    # 마지막 좌표의 복구시간 반환
    return recovery_times[-1][-1]


T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 지도의 크기 정보
    map_lst = [list(map(int, input())) for _ in range(N)]  # 지도 정보

    # 함수 호출 및 결과 출력
    result = find_min_recovery_time()
    print(f'#{tc}', result)