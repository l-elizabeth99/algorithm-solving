import sys
sys.stdin = open('input.txt')


class CQueue:
    def __init__(self, size=16):
        self.front = 0
        self.rear = 0
        self.container = [0] * size
        self.size = size

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def is_empty(self):
        return self.rear == self.front

    def enqueue(self, value):
        if self.is_full():
            raise ValueError('Q is full')
        else:
            self.rear = (self.rear + 1) % self.size
            self.container[self.rear] = value

    def dequeue(self):
        if self.is_empty():
            raise ValueError('Q is empty')
        else:
            self.front = (self.front + 1) % self.size
            return self.container[self.front]


T = 10
for tc in range(1, T+1):
    _ = input()
    N = 16  # 미로의 크기
    maze = [input() for _ in range(N)]

    # 방문 표시를 위한 리스트 - 미로의 크기와 동일
    visited = [[False] * N for _ in range(N)]
    q = CQueue(N*N)  # 미로의 크기만큼 q 생성

    # 시작점('2') 찾기
    for r in range(N):
        for c in range(N):
            if maze[r][c] == '2':
                # r, c 가 시작점 - q에 넣고 종료
                q.enqueue((r, c))
                break

    # BFS로 모든 길 탐색, 도착점(3)에 도착 시 종료
    result = 0

    # 큐가 비어있지 않으면
    while not q.is_empty():
        # 큐에 있는 값을 디큐
        row, col = q.dequeue()

        # 해당 위치가 방문하지 않은 곳이면
        if not visited[row][col]:
            # 방문 표시
            visited[row][col] = True
            if maze[row][col] == '3':
                result = 1  # 도착점에 도착하면 결과를 가능하다고 표시
                break
            # 반복하며 연결된 다른 곳(상하좌우)이 있는지 확인
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = row + dr
                nc = col + dc
                if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != '1':
                    # 한 번도 방문하지 않은 곳이면
                    if not visited[nr][nc]:
                        # 해당 위치를 인큐
                        q.enqueue(((nr, nc)))

    print(f'#{tc}', result)