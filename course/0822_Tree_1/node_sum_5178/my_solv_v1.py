import sys
sys.stdin = open('5178_input.txt')


def pre_order(edge):  # 전위 순회 함수
    if edge:  # 정점이 있으면
        print(edge)  # 해당 정점 출력
        pre_order(left[edge])  # 해당 정점의 왼쪽을 정점으로 한 자식으로 갱신
        pre_order(right[edge])  # 해당 정점의 오른쪽을 정점으로 한 자식으로 갱신


T = int(input())  # 테스트 케이스 수
for tc in range(1, T+1):  # 테스트 케이스만큼 반복
    N, M, L = map(int, input().split())  # 노드의 수, 리프 노드의 수, 출력해야 하는 노드의 번호

    tree = [0] * (N+1)  # 트리 생성

    # 리프 노드에 대한 정보(리프 노드의 번호, 해당 노드의 숫자)
    leaf_node_info = [list(map(int, input().split())) for _ in range(M)]

    # 리프 노드의 수만큼 반복하며 트리의 리프 노드의 값을 숫자로 지정
    for i in range(M):
        leaf_num = leaf_node_info[i][0]
        num = leaf_node_info[i][1]
        tree[leaf_num] = num

    # 리프 노드부터 루트 노드까지 반복 - 끝 번호부터 시작해야 함
    for curr_node in range(N, 0, -1):
        # 현재 노드가 리프 노드가 아니면
        if tree[curr_node] == 0:
            # 현재 노드의 값을 왼쪽 자식과 오른쪽 자식 노드의 값을 더한 값으로 지정

            # # 현재 노드의 왼쪽 자식 노드가 트리의 범위에 있으면
            # # # 현재 노드의 오른쪽 자식 노드가 존재하지 않음 -> 왼쪽 자식만 더하기
            if curr_node*2 <= N:
                tree[curr_node] += tree[curr_node*2]

            # # 현재 노드의 오른쪽 자식 노드가 트리의 범위에 있으면
            # # # 현재 노드의 오른쪽 자식 노드가 존재하지 않음 -> 왼쪽 자식만 더하기
            if curr_node*2 + 1 <= N:
                tree[curr_node] += tree[curr_node*2 + 1]

    print(f'#{tc}', tree[L])  # 결과 출력