import sys
sys.stdin = open('sample_input.txt')

T = int(input())  # 테스트 케이스 수
for tc in range(1, T+1):  # 테스트 케이스만큼 반복
    N, M = map(int, input().split())  # 정수의 개수, 구간의 개수
    a = list(map(int, input().split()))  # N개의 정수

    first_sum = 0  # 첫번째 구간의 합을 0으로 지정
    for num in range(M):  # M만큼 반복
        first_sum += a[num]  # 첫번째 구간의 합에 현재 숫자를 더함

    max_sum = first_sum  # 최대 합을 첫번째 구간의 합으로 지정
    min_sum = first_sum  # 최소 합을 첫번째 구간의 합으로 지정
    for i in range(1, N-M+1):  # N-M만큼 반복
        curr_sum = 0  # 현재 구간의 합을 0으로 지정
        for j in range(M):  # M만큼 반복
            curr_sum += a[i+j]  # 현재 구간의 합에 현재 숫자를 더함

        if curr_sum > max_sum:  # 현재 구간의 합이 최대 합보다 크다면
            max_sum = curr_sum  # 최대 합을 현재 구간의 합으로 갱신

        if curr_sum < min_sum:  # 현재 구간의 합이 최소 합보다 작다면
            min_sum = curr_sum  # 최소 합을 현재 구간의 합으로 갱신

    diff = max_sum - min_sum  # 최대 합과 최소 합의 차이를 지정

    print(f'#{tc}', diff)  # 결과 출력