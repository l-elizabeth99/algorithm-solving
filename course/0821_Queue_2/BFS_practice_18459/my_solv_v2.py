import sys
sys.stdin = open('input.txt')

from collections import deque


class Path:
    def __init__(self, vertex_num):
        self.vertex_num = vertex_num
        self.adj_list = [[] for _ in range(vertex_num + 1)]

    def add_edge(self, left, right):
        self.adj_list[left].append(right)
        self.adj_list[right].append(left)

    def bfs(self, start_node):
        visited = [0] * (self.vertex_num + 1)
        q = deque()
        q.append(start_node)
        visited[start_node] = 1

        path_list = []
        while q:
            curr_node = q.popleft()
            path_list.append(curr_node)
            for next_node in self.adj_list[curr_node]:
                if visited[next_node] == 0:
                    visited[next_node] = visited[curr_node] + 1
                    q.append(next_node)

        return path_list


V, E = map(int, input().split())
edge_info = list(map(int, input().split()))

p = Path(V)
for i in range(E):
    start, end = edge_info[i*2], edge_info[i*2 + 1]
    p.add_edge(start, end)

bfs_path = p.bfs(1)

print(f'#1', *bfs_path)