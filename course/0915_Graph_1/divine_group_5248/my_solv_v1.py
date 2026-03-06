import sys
sys.stdin = open('sample_input.txt')


def dfs(curr_node):
    # 갈 수 있는 노드를 반복하며 이미 방문했으면 종료
    for next_node in graph[curr_node]:
        if visited[next_node]:
            continue

        # 갈 수 있으면 방문 처리 후 재귀 호출
        visited[next_node] = 1
        dfs(next_node)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # 출석번호 수, 신청서 수

    graph = [[] for _ in range(N+1)]  # 인접 리스트 - 연결된 간선 저장
    visited = [0] * (N+1)  # 방문 기록

    # 번호 리스트
    num_lst = list(map(int, input().split()))

    # 신청서 수의 두배만큼 반복하며
    # 번호 리스트에서 이전 수와 이후 수를 가져온 후 두 수를 양방향으로 저장
    for num in range(0, M*2, 2):
        before_num = num_lst[num]
        after_num = num_lst[num+1]
        graph[before_num].append(after_num)
        graph[after_num].append(before_num)

    cnt = 0  # 조 개수 초기화

    # 출석번호 수만큼 반복하며 현재 노드가 방문하지 않은 곳이면 함수 호출 후 조 개수 증가
    for node in range(1, N+1):
        if visited[node] == 0:
            dfs(node)
            cnt += 1

    # 조 개수 출력
    print(f'#{tc}', cnt)