# visited 생성 (2차원 배열로 생성)
# 큐 생성, 시작점 인큐 (4, 3)
# 인큐 표시 - visited에 1 넣기
# 반복
    # 디큐 (4, 3)
    # 방문해서 할 일(maze[i][j] = 3이면 할 일)
    # 방문 정점에 인접(상하좌우 중 벽(1)이 아닌 것)하고 미방문(visited[ni][nj] == 0)이면
        # 인큐
        # 인큐 표시


def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j


def bfs(i, j, N):
    visited = [[0] * N for _ in range(N)]  # visited 생성 (2차원 배열로 생성)
    q = [[i, j]]  # 큐 생성, 시작점 인큐 (4, 3)
    visited[i][j] = 1  # 인큐 표시 - visited에 1 넣기
    while q:  # 반복
        ti, tj = q.pop(0)  # 디큐 (4, 3)
        if maze[ti][tj] == 3:  # 방문해서 할 일(maze[i][j] = 3이면 할 일)
            return visited[ti][tj] - 2
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            wi, wj = ti + di, tj + dj
            # 유효성 검사, 벽이 아닌 것, 간 적 없은 곳이면
            if 0 <= wi < N and 0 <= wj < N and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                q.append([wi, wj])  # 인큐
                visited[wi][wj] = visited[ti][tj] + 1  # 인큐 표시
    return 0


N = int(input())
maze = [list(map(int, input())) for _ in range(N)]
start_i, start_j = find_start(N)
ans = bfs(start_i, start_j, N)
print(ans)