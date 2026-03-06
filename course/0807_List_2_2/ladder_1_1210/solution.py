import sys
sys.stdin = open('input.txt')

    # 사다리는 좌, 우를 우선으로 판별 / 갈 수 있으면 이동
        # 좌, 우로도 갈 수 없으면 위로 이동
        # 특정 지점에서 무한 루프에 빠질 가능성 존재
            # 왔던 길을 0으로 초기화하여 되돌아가지 못하게 함

T = 10
N = 100
for tc in range(1, T+1):
    _ = input()
    ladder = [input().split() for _ in range(N)]

    # 시작 지점을 찾기 위해서는 도착지점에서부터 출발해야 한 번에 찾을 수 있음
    now = [99, 0]  # 현재 위치를 나타내는 리스트 좌표 - 99:마지막 줄
    for j in range(N):
        if ladder[99][j] == '2':  # 도착지점
            now[1] = j  # 도찾지점을 현재 위치에 저장
            break

    # 이동 가능 방향 [좌, 우, 상] - 좌우를 먼저 확인한 후 위로 가도록 리스트 작성
    dr = [0, 0, -1]
    dc = [-1, 1, 0]

    # 사다리의 이동은 행이 0이 될 때까지 반복
    while now[0] != 0:
        for idx in range(3):  # 3:방향의 개수(좌 확인->우 확인->상 확인)
            # 델타만큼 다음 행열 좌표 계산
            nr = now[0] + dr[idx]
            nc = now[1] + dc[idx]

            # 계산된 좌표가 이동가능한 범위인지 확인
            if 0 <= nr < N and 0 <= nc < N and ladder[nr][nc] == '1':
                # 이전 위치(왔던 길)를 3으로 표시
                ladder[now[0]][now[1]] = '3'

                # 현재 위치를 갱신
                now[0] = nr
                now[1] = nc
                break  # 다른 방향 탐색 불필요

    print(f'#{tc}', now[1])