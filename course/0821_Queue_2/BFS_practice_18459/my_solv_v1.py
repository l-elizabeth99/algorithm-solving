import sys
sys.stdin = open('input.txt')

from collections import deque

'''
테스트 케이스 = 1
테스트 케이스만큼 반복하며
    정점의 개수, 간선의 개수 받기
    간선의 정보를 리스트로 받기 - 간선 리스트
    경로를 빈 인접 리스트로 생성(정점의 수보다 하나 많게 생성) - 경로 리스트
    간선의 수만큼 반복하며
        간선의 정보쌍을 지정하고
        양방향으로 경로 리스트에 저장
    방문한 곳을 담을 리스트 생성(정점의 수보다 하나 많게 0으로 만들어진 리스트) - 방문 리스트
    큐 생성
    시작점을 1로 지정하고 큐에 넣기
    시작점에 방문 표시
    
    결과 양식 출력
    큐가 빌 때까지 반복하며
        큐에서 뺀 값을 출력
        큐에서 뺀 값의 경로 리스트만큼 반복하며
            해당 지점이 방문하지 않은 곳이면
                해당 지점을 큐에 넣고
                해당 지점의 방문 여부를 큐에서 뺀 값의 1을 더한 값으로 갱신
'''

T = 1
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))
    path_list = [[] for _ in range(V + 1)]
    for p in range(E):
        path_1, path_2 = arr[p*2], arr[p*2 + 1]
        path_list[path_1].append(path_2)
        path_list[path_2].append(path_1)

    visited = [0] * (V+1)
    q = deque()
    start = 1

    q.append(start)
    visited[start] = 1

    print(f'#{tc}', end=' ')

    while q:
        path = q.popleft()
        print(path, end=' ')
        for lst in path_list[path]:
            if visited[lst] == 0:
                q.append(lst)
                visited[lst] = visited[path] + 1
