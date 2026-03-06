import sys
sys.stdin = open('sample_input.txt')

from heapq import heappop, heappush


def dijkstra(start_row, start_col):
    # 상하좌우 델타 값
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    pq = [(0, start_row, start_col)]  # 연료 소비량, r, c
    dists = [[float('inf')] * N for _ in range(N)]  # 최소 연료 소비량
    dists[start_row][start_col] = 0  # 출발지 초기화

    # pq가 빌 때까지 반복
    while pq:
        # pq에서 뺀 값을 연료, 좌표로 지정
        curr_fuel, curr_row, curr_col = heappop(pq)

        # 현재 좌표의 최소 연료가 현재 연료보다 작으면 종료
        if dists[curr_row][curr_col] < curr_fuel:
            continue

        # 좌표가 끝까지 왔다면 최소 연료를 반환
        if curr_row == (N-1) and curr_col == (N-1):
            return dists[-1][-1]

        # 4방향만큼 반복
        for k in range(4):
            # 새로운 좌표를 지정
            nr, nc = curr_row + dr[k], curr_col + dc[k]

            # 새로운 좌표가 유효한 위치에 있다면
            if 0 <= nr < N and 0 <= nc < N:
                # 현재 높이와 다음 높이 지정 후 새 연료를 계산
                curr_height = H_lst[curr_row][curr_col]
                next_height = H_lst[nr][nc]
                new_fuel = curr_fuel + 1 + max(0, (next_height - curr_height))

                # 새로운 좌표의 누적 최소 연료가 새로운 연료보다 작거나 같으면 종료
                if dists[nr][nc] <= new_fuel:
                    continue

                # 새로운 좌표의 연료를 새 연료로 지정 후 pq에 새 연료와 새로운 좌표 넣기
                dists[nr][nc] = new_fuel
                heappush(pq, (new_fuel, nr, nc))
    # 최소 연료 반환
    return dists[-1][-1]


T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 가로, 세로 칸 수
    H_lst = [list(map(int, input().split())) for _ in range(N)]  # N개의 높이 정보

    # 함수 호출 및 결과 출력
    result = dijkstra(0, 0)
    print(f'#{tc}', result)