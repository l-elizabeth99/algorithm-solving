import sys
sys.stdin = open('s_input.txt')

T = int(input())  # 테스트 케이스 수
for tc in range(1, T+1):  # 테스트 케이스만큼 반복
    N = int(input())  # 버스 노선 수
    bus_stops = [0] * 5001  # 0을 구성된 버스 정류장 배열 생성
    for _ in range(N):  # 버스 노선 수만큼 반복
        A, B = list(map(int, input().split()))  # 버스 정류장의 시작 구간, 마지막 구간
        for i in range(A, B+1):  # 시작 정류장부터 마지막 정류장까지 반복
            bus_stops[i] += 1  # i번째에 해당하는 배열에 1을 추가

    P = int(input())  # 버스 정류장 수
    count_bus_stops= []  # 버스 정류장을 지나는 버스 노선의 수를 담을 빈 리스트 생성
    for _ in range(P):  # 버스 정류장 수만큼 반복
        C = int(input())  # 버스 정류장 번호
        count_bus_stops.append(bus_stops[C])  # 버스 정류장 번호에 해당하는 배열의 값을 빈 리스트에 담기

    print(f'#{tc}', *count_bus_stops)  # 결과 출력