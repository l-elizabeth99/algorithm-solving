import sys
sys.stdin = open('sample_input.txt')

from heapq import heappop, heappush


def dijkstra(start_node):
    pq = [(0, start_node)]  # 누적 거리, 노드 번호
    dist = [float('inf')] * (N+1)  # 최단 거리
    dist[start_node] = 0  # 시작점 초기화

    # pq가 빌 때까지 반복
    while pq:
        # pq에서 뺀 값을 현재 거리, 현재 노드로 지정
        curr_dist, curr_node = heappop(pq)

        # 현재 노드의 최단 거리가 현재 길이보다 작으면 종료
        if dist[curr_node] < curr_dist:
            continue

        # 다음 거리와 다음 노드를 반복
        for next_dist, next_node in graph[curr_node]:
            # 새 거리를 현재 거리와 다음 거리의 합으로 지정
            new_dist = curr_dist + next_dist

            # 다음 노드의 최단 거리가 새 거리보다 작거나 같으면 종료
            if dist[next_node] <= new_dist:
                continue

            # 다음 노드의 최단 거리를 새 거리로 지정 후 pq에 새 거리와 다음 노드 넣기
            dist[next_node] = new_dist
            heappush(pq, (new_dist, next_node))

    # 최단 거리 반환
    return dist[-1]


T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())  # 연결 지점 개수, 도로 개수
    graph = [[] for _ in range(N+1)]  # 인접 리스트

    # 도로 개수만큼 반복하며 시작점에 거리와 끝점을 저장
    for _ in range(E):
        s, e, w = map(int, input().split())  # 시작점, 끝점, 거리
        graph[s].append((w, e))  # 단방향

    # 함수 호출 및 결과 출력
    result = dijkstra(0)
    print(f'#{tc}', result)