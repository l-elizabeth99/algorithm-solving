import sys
sys.stdin = open('input.txt')

T = 1
for tc in range(1, T+1):
    V, E = map(int, input().split())  # 정점의 수, 간선의 수
    num = list(map(int, input().split()))  # 간선의 수만큼 연결된 정점
    lists = [[] for _ in range(V+1)]  # 정점의 수보다 하나 많은 수의 빈 리스트 생성
    for i in range(E):  # 간선의 수만큼 반복
        start = num[i*2]  # 시작점을 왼쪽으로 지정
        end = num[i*2+1]  # 끝점을 오른쪽으로 지정
        lists[start].append(end)
        lists[end].append(start)

        print(lists)