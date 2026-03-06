import sys
sys.stdin = open('sample_input.txt')

from heapq import heappop, heappush


def prim(start_node):
    pq = [(0, start_node)]  # 가중치, 시작 노드
    MST = [0] * (V+1)  # 방문 기록
    total_weight = 0  # 가중치 초기화
    cnt = 0  # 노드 개수

    # pq가 빌 때까지 반복
    while pq:
        # pq에서 뺀 값을 가중치, 노드로 지정
        weight, node = heappop(pq)

        # 해당 노드를 방문한 적 있으면 종료
        if MST[node]:
            continue

        # 방문 기록 및 가중치 누적, 노드 개수 증가
        MST[node] = 1
        total_weight += weight
        cnt += 1

        # 다음 가중치와 다음 노드를 순회
        for next_weight, next_node in edges[node]:
            # 다음 노드를 방문한 적 있으면 종료
            if MST[next_node]:
                continue

            # pq에 다음 가중치와 다음 노드 넣기
            heappush(pq, (next_weight, next_node))

    # 가중치 반환
    return total_weight


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())  # 노드 개수, 간선 개수
    edges = [[] for _ in range(V+1)]  # 인접 리스트
    
    # 간선 수만큼 반복하며 양방향을 저장
    for _ in range(E):
        start, end, weight = map(int, input().split())
        edges[start].append((weight, end))
        edges[end].append((weight, start))

    # 함수 호출 및 결과 출력
    result = prim(0)
    print(f'#{tc}', result)