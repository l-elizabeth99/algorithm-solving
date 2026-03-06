import sys
sys.stdin = open('sample_input.txt')


def find_set(x):
    if x != parent[x]:
        parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x < root_y:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]

    result = 0
    edges.sort(key=lambda x: x[2])
    parent = list(range(V+1))

    for start, end, weight in edges:
        if find_set(start) != find_set(end):
            union(start, end)
            result += weight

    print(f'#{tc}', result)