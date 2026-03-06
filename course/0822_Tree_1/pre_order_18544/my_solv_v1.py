import sys
sys.stdin = open('input.txt')


def pre_order(T):  # 전위 순회 함수 지정 - 정점의 번호를 받기
    if T:  # 정점이 존재하면
        print(T, end=' ')  # 해당 정점을 출력
        pre_order(left[T])  # 해당 정점의 왼쪽 자식으로 이동
        pre_order(right[T])  # 해당 정점의 오른쪽 자식으로 이동


V = int(input())  # 정점의 수
E = V - 1  # 간선의 수
arr = list(map(int, input().split()))  # 간선 정보(부모 자식 순)

left = [0] * (V+1)  # 왼쪽 자식에 대한 정보를 담을 리스트 생성 - 부모를 기준으로 저장
right = [0] * (V+1)  # 오른쪽 자식에 대한 정보를 담을 리스트 생성 - 부모를 기준으로 저장
parent = [0] * (V+1)  # 부모 노드에 대한 정보를 담을 리스트 생성 - 자식을 기준으로 저장

for i in range(E):  # 간선의 수만큼 반복하며
    p, c = arr[i*2], arr[i*2 + 1]  # 부모 정점과 자식 정점 정보 지정
    parent[c] = p  # 부모 정보의 자식 인덱스 값을 부모 인덱스로 지정

    if left[p] == 0:  # 왼쪽 자식 정보에 부모 인덱스가 없으면
        left[p] = c  # 해당 값을 자식 인덱스로 갱신
    else:  # 오른쪽 자식 정보에 부모 인덱스가 없으면
        right[p] = c  # 해당 값을 자식 인덱스로 갱신

root_num = 1  # 정점의 번호를 1로 지정
for n in range(1, V+1):  # 1부터 정점의 수까지 반복하며
    if parent[n] == 0:  # 부모 정보에 해당 정점의 값이 없으면
        root_num = n  # 정점의 번호를 현재 정점으로 갱신하고
        break  # 종료

pre_order(root_num)  # 전위 순회 함수 호출