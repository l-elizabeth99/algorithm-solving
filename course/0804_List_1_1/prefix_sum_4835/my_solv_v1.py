import sys
sys.stdin = open('sample_input.txt')

T = int(input())  # 테스트 케이스 수 받기

for tc in range(1, T+1):  # 테스트 케이스만큼 반복
    N, M = map(int, input().split())  # 정수의 개수, 구간의 개수 받기
    a = list(map(int, input().split()))  # N개의 정수 받기

    first_total = 0  # 첫번째 구간의 합을 0으로 설정

    for k in range(M):  # M번 반복
        first_total += a[k]  # 첫번째 구간의 합에 현재 인덱스 값을 더하기

    max_total = first_total  # 최대 합을 담을 변수 생성 - 첫번째 구간의 합으로 지정
    min_total = first_total  # 최소 합을 담을 변수 생성 - 첫번째 구간의 합으로 지정

    for i in range(N - M + 1):  # N-M번 반복
        total = 0  # 현재 합을 담을 변수 생성 - 0으로 지정
        for j in range(M):  # M번 반복
            total += a[i+j]  # 현재 값에 현재 인덱스부터 j번째 인덱스까지의 합(M번 더한 값)을 더하기

        if total > max_total:  # 현재 합이 최대 합보다 크다면
            max_total = total  # 최대 합을 현재 합으로 갱신

        if total < min_total:  # 현재 합이 최소 합보다 작다면
            min_total = total  # 최소 합을 현재 합으로 갱신

    results = max_total - min_total  # 최대 합과 최소 합의 차이를 담을 변수 생성

    print(f'#{tc}', results)  # 결과 출력