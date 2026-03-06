import sys
sys.stdin = open('5105_input.txt')

from collections import deque

'''
테스트 케이스 받기
테스트 케이스만큼 반복하며
    미로의 크기 받기
    미로의 정보를 2차원 리스트에 담기
    시작점을 찾기(행 먼저 순회하며 2인 곳 찾기)
    큐 생성(i, j를 튜플로 저장)
    큐가 없을 때까지 반복하며
        현재 위치를 큐에서 꺼내기
        현재 위치에서 상하좌우로 1이 아닌 곳만 방문
            방문한 곳을 현재 위치에서 1을 더한 값으로 표시
        현재 위치기 3이면 찾기 중지
            움직인 수(현재 위치의 값에서 2을 뺀 값) 구하기
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start_i, start_j = i, j

    visited = [[0] * N for _ in range(N)]
    q = deque([(start_i, start_j)])
    visited[start_i][start_j] = 1

    min_count = 0
    while q:
        curr_i, curr_j = q.popleft()
        if maze[curr_i][curr_j] == 3:
            min_count = visited[curr_i][curr_j] - 2
            break

        di = [0, 1, 0, -1]
        dj = [1, 0, -1, 0]
        for k in range(4):
            ni = curr_i + di[k]
            nj = curr_j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                    q.append((ni, nj))
                    visited[ni][nj] = visited[curr_i][curr_j] + 1

    print(f'#{tc}', min_count)