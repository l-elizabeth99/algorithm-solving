import sys
sys.stdin = open('input.txt')

T = int(input())  # 테스트 케이스 수
for tc in range(1, T+1):  # 테스트 케이스만큼 반복
    N = int(input())  # 양수의 개수
    a = list(map(int, input().split()))  # N개의 양수

    max_value = a[0]  # 가장 큰 수를 첫번째 값으로 지정
    min_value = a[0]  # 가장 작은 수를 첫번째 값으로 지정
    for i in range(N):  # 양수의 개수만큼 반복
        if a[i] > max_value:  # 현재 값이 가장 큰 수보다 크다면
            max_value = a[i]  # 가장 큰 수를 현재값으로 갱신
        if a[i] < min_value:  # 현재 값이 가장 작은 수보다 작다면
            min_value = a[i]  # 가장 작은 수를 현재값으로 갱신

    diff = max_value - min_value  # 가장 큰 수와 가장 작은 수의 차이를 지정
    print(f'#{tc}', diff)