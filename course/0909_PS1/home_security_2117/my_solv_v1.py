import sys
sys.stdin = open('sample_input.txt')

'''
서비스 영역 = K
도시 크기 = N
한 집에서의 지불 비용 = M

운영 비용 = K * K + (K -1) * (K - 1)
수익 = 집의 개수 * M
이익 = 수익 - 운영 비용 : 이익 >= 0

K : 1~N까지 반복
중심 위치 : (x, y) : (0, 0) ~ (N-1, N-1)
서비스 영역 범위 : 절댓값(중심 위치-현재 위치)
'''

T = int(input())  # 테스트 케이스
for tc in range(1, T+1):  # 테스트 케이스만큼 반복
    N, M = map(int, input().split())  # 도시 크기, 하나의 집에서 지불하는 비용
    city_arr = [list(map(int, input().split())) for _ in range(N)]  # 도시 정보

    houses = []  # 집의 위치를 담을 리스트
    # 전체를 돌며 해당 위치가 집인 지점을 리스트에 담기
    for i in range(N):
        for j in range(N):
            if city_arr[i][j] == 1:
                houses.append((i, j))

    max_houses = 0  # 최대 가구 수
    # 전체를 순회하며 서비스 영역 결정 및 운영 비용, 현재 가구 수, 최대 가구 수 계산
    for r in range(N):
        for c in range(N):

            # 서비스 영역을 돌며 운영 비용 계산
            for K in range(1, N*2):
                costs = K**2 + (K-1)**2

                curr_houses = 0  # 현재 가구 수
                # houses를 돌며 거리가 서비스 영역 안이면 현재 가구 수 증가
                for houses_r, houses_c in houses:
                    distance = abs(r - houses_r) + abs(c - houses_c)
                    if distance < K:
                        curr_houses += 1

                # 이익이 있으면 현재 가구 수와 최대 가구 수를 비교해 최대 가구 수 갱신
                if curr_houses * M >= costs:
                    if curr_houses > max_houses:
                        max_houses = curr_houses

    print(f'#{tc}', max_houses)  # 최대 가구 수 출력