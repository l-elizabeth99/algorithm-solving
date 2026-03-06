import sys
sys.stdin = open('s_input.txt')

T = int(input())  # 테스트 케이스 수

for tc in range(1, T + 1):
    N = int(input())  # 버스 노선 수

    bus_stops = [0] * 5001  # 크기가 5001인 배열 생성

    for _ in range(N):
        A, B = map(int, input().split())  # 버스 번호
        for i in range(A, B + 1):  # A부터 B까지 반복(B+1번째는 포함하지 않음)
            bus_stops[i] += 1  # 버스 정류장의 수를 갱신

    P = int(input())  # 버스 정류장 수

    counts = []  # 해당 버스 정류장을 담을 빈 리스트 생성

    for _ in range(P):
        C = int(input())  # 버스 정류장 번호
        counts.append(bus_stops[C])  # 해당 버스 정류장 번호를 리스트에 담음

    print(f'#{tc}', *counts)  # 결과를 출력
