import sys
sys.stdin = open('5201_input.txt')

# 트럭당 한 개의 컨테이너를 운반 가능
# 적재용량을 초과하는 컨테이너는 운반 불가능
# 트럭당 편도로 한 번만 운행 가능
# 이동한 화물의 총 중량 중 최대인 경우의 무게 출력
# 화물을 싣지 못 할 수 있음, 화물이 남을 수 있음
# 모든 트럭이 컨테이너를 옮길 수 없다면 0을 출력

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # 컨테이너 수, 트럭 수
    weight_container = list(map(int, input().split()))  # N개의 화물 무게
    full_weight = list(map(int, input().split()))  # M개의 트럭의 적재 용량

    weight_container.sort(reverse=True)  # 화물 무게를 내림차순으로 정렬
    full_weight.sort(reverse=True)  # 적재 용량을 내림차순으로 정렬

    total_weight = 0  # 전체 무게
    container_idx = 0  # 컨테이너 인덱스
    truck_idx = 0  # 트럭 인덱스

    # 컨테이너 인덱스가 컨테이너의 수보다 작고, 트럭의 인덱스가 트럭의 수보다 작으면 계속 반복
    while container_idx < N and truck_idx < M:
        # 현재 컨테이너 무게가 현재 트럭의 적재 용량 이하면
        if weight_container[container_idx] <= full_weight[truck_idx]:
            total_weight += weight_container[container_idx]  # 전체 무게에 현재 화물 무게 누적
            container_idx += 1  # 컨테이너 인덱스 증가
            truck_idx += 1  # 트럭 인덱스 증가
        else:  # 그 외에는 컨테이너 인덱스만 증가
            container_idx += 1

    # 결과 출력
    print(f'#{tc}', total_weight)