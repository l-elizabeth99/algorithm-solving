import sys
sys.stdin = open('sample_input.txt')

T = int(input())  # 테스트 케이스 수
for tc in range(1, T+1):  # 테스트 케이스만큼 반복
    N = int(input())  # 양수의 개수
    arr = list(map(int, input().split()))  # N개의 양수

    min_v = arr[0]  # 최소값을 리스트의 첫번째로 설정
    min_idx = 0  # 최소값의 인덱스를 0으로 설정

    max_v = arr[0]  # 최대값을 리스트의 첫번째로 설정
    max_idx = 0  # 최대값의 인덱스를 0으로 설정

    for i in range(1, N):  # N번 반복
        if arr[i] < min_v:  # 현재 값이 최소값보다 작으면
            min_v = arr[i]  # 최소값을 현재 값으로 갱신
            min_idx = i  # 최소값의 인덱스를 현재 인덱스로 갱신

        if arr[i] >= max_v:  # 현재 값이 최대값보다 크거나 같으면
            max_v = arr[i]  # 최대값을 현재 값으로 갱신
            max_idx = i  # 최대값의 인덱스를 현재 인덱스로 갱신

    diff = abs(max_idx - min_idx)  # 최대값의 인덱스와 최소값의 인덱스의 차이를 설정

    print(f'#{tc}', diff)  # 결과 출력