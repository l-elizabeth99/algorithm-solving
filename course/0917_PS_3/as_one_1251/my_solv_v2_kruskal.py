import sys
sys.stdin = open('re_sample_input.txt')


def find_set(c):
    # 자식이 부모이면 자식을 반환
    if c == parent[c]:
        return c

    # 찾은 부모를 나의 부모로 갱신 후 부모 반환
    parent[c] = find_set(parent[c])
    return parent[c]


def union(x, y):
    # x의 부모와 y의 부모를 찾기
    rx = find_set(x)
    ry = find_set(y)

    # 부모가 같으면 합치기 실패
    if rx == ry:
        return False

    # y의 부모를 x로 갱신 후 합치기 성공
    parent[ry] = rx
    return True


T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 섬 개수
    X = list(map(int, input().split()))  # x 좌표
    Y = list(map(int, input().split()))  # y 좌표
    E = float(input())  # 환경 부담 세율 실수

    # 간선 정보 및 모든 노드의 부모를 자기 자신으로 초기화
    edges = []
    parent = [p for p in range(N)]

    # 모든 쌍에 대한 거리의 제곱값을 계산해 간선 정보에 쌍의 좌표와 함께 넣기
    for i in range(N):
        for j in range(i+1, N):
            squared_dist = (X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2
            edges.append((squared_dist, i, j))

    # 간선을 거리의 제곱값을 기준으로 오름차순 정렬
    edges.sort()

    # 총 거리의 제곱값과 선택한 간선의 수 초기화
    total_squared_dist = 0
    cnt = 0

    # 간선 정보를 순회하며 시작점과 끝점을 합칠 수 있으면 총 거리의 제곱값에 제곱값 누적 및 간선의 수 증가
    for dist, start, end in edges:
        if union(start, end):
            total_squared_dist += dist
            cnt += 1

        # 선택한 간선의 수가 모든 간선의 수와 같아지면 종료
        if cnt == N-1:
            break

    # 결과 계산 및 출력
    result = E * total_squared_dist
    print(f'#{tc} {result:.0f}')