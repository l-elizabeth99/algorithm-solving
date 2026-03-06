# 목적 : 조망권(좌우로 2칸)이 확보된 세대의 수 구하기
# 현재 빌딩 옆에 현재 빌딩보다 높은 건물이 있다면 그 빌딩은 조망권 확보 x
# 없다면 좌우로 2칸 옆의 빌딩 중 가장 큰 빌딩의 높이를 찾기
# 현재 빌딩의 조망권 = 현재 빌딩 높이 - 위의 빌딩 높이

import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    # N: 건물의 개수 (4 <= N <= 1000)
    # N개의 건물 높이가 주어짐 (0 <= 건물 높이 <= 255)
    N = int(input())
    building_list = list(map(int, input().split()))
    
    # print(N, building_list)
    # 전체 조망권의 개수 구해야 함
    # 모든 빌딩을 반복
        # l2 ~ r2 빌딩이 현재 빌딩보다 낮다면
            # 조망권 = 현재 빌딩 높이 - max(l2, l1, r1, r2)
            # 조망권 누적

    # 모든 빌딩에 대해 반복
    total_view = 0
    for idx in range(N):  # idx: 현재 빌딩
        # 빌딩이 없으면 제외
        if building_list[idx] == 0:
            continue  # 다음 빌딩으로
            
        current = building_list[idx]  # 현재 빌딩 높이
        left2 = building_list[idx - 2]  # l2
        left1 = building_list[idx - 1]  # l1
        right1 = building_list[idx + 1]  # r1
        right2 = building_list[idx + 2]  # r2

        heights_near_building = 0
        # 조망권이 존재
        if (current > left2) and (current > left1) and (current > right1) and (current > right2):

            # l2 ~ r2 중 가장 높은 빌딩 찾기
            if heights_near_building < left2:
                heights_near_building = left2

            if heights_near_building < left1:
                heights_near_building = left1

            if heights_near_building < right1:
                heights_near_building = right1

            if heights_near_building < right2:
                heights_near_building = right2

            # print(heights_near_building)  # 가장 높은 빌딩
            view = current - heights_near_building  # 조망권 계산
            total_view += view  # 조망권 누적

    print(f'#{tc} {total_view}')