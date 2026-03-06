import sys
sys.stdin = open('sample_input.txt')

import heapq


def search(start, acc_dist):
    global result

    candidate = []
    for next_info in graph[start]:
        candidate.append(next_info)

    visited[start] = 1

    heapq.heapify(candidate)
    while candidate:
        weight, now = heapq.heappop(candidate)

        if not visited[now]:
            result += weight
            visited[now] = 1
            for weight, next in graph[now]:
                if not visited[next]:
                    heapq.heappush(candidate, [weight, next])


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]

    result = 0
    visited = [0] * (V+1)
    graph = {start: [] for start in range(V+1)}

    for start, end, weight in edges:
        graph[start].append([weight, end])
        graph[end].append([weight, start])

    search(0, 0)

    print(f'#{tc}', result)