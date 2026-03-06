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
    city = [list(map(int, input().split())) for _ in range(N)]  # 도시 정보
    max_houses = 0  # 서비스를 제공받는 최대 가구 수
    # 서비스 영역의 크기가 될 수 있는 값만큼 순회 - 서비스 영역의 크기가 전체일 때까지 반복
    for K in range(1, N*2):
        cost = K**2 + (K-1)**2  # 운영 비용 계산
        # 서비스 영역의 순회 - 큰 틀 - 행 먼저 순회
        for i in range(N):
            for j in range(N):
                curr_houses = 0  # 현재 서비스를 제공받는 가구 수
                # 서비스 영역 순회 - 영역 이내 - 행 먼저 순회
                for p in range(N):
                    for q in range(N):
                        distance = abs(i - p) + abs(j - q)  # 현재 위치로부터 서비스 영역 크기 거리 계산
                        if distance < K:  # 거리가 서비스 영역의 크기보다 작을 경우
                            if city[p][q] == 1:  # 현재 위치가 집이라면
                                curr_houses += 1  # 현재 가구 수 증가
                revenue = curr_houses * M  # 수익 계산
                profit = revenue - cost  # 이익 계산
                if profit >= 0:  # 이익이 있을 경우
                    if curr_houses > max_houses:  # 현재 가구 수가 최대 가구 수보다 크면
                        max_houses = curr_houses  # 최대 가구 수를 현재 가구 수로 갱신
    print(f'#{tc}', max_houses)  # 최대 가구 수 출력