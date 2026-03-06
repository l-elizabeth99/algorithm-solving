import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]

    result = 0
    edges.sort(key=lambda x: x[2])
    visited = [0] * (V+1)

    for start, end, weight in edges:
        if not visited[start] or not visited[end]:
            visited[start] = 1
            visited[end] = 1
            result += weight

    print(f'#{tc}', result)