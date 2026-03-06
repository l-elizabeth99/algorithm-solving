import sys
sys.stdin = open('input.txt')

T = 10  # 테스트 케이스 수

for tc in range(1, T+1):  # 테스트 케이스만큼 반복
    tc_n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]  # 입력을 2차원 배열에 저장

    max_v = 0  # 최대 합을 0으로 설정

    # 행의 합 계산
    for i in range(100):  # 행 순회
        sum_i = 0  # 초기 행의 합을 0으로 설정

        for j in range(100):  # 열 순회
            sum_i += arr[i][j]  # 행의 합 갱신

        if sum_i > max_v:  # 현재 행의 합이 최대 합보다 크다면
            max_v = sum_i  # 최대 합 갱신

    # 열의 합 계산
    for j in range(100):  # 열 순회
        sum_j = 0  # 초기 열의 합을 0으로 설정

        for i in range(100):  # 행 순회
            sum_j += arr[i][j]  # 열의 합 갱신

        if sum_j > max_v:  # 현재 열의 합이 최대 합보다 크다면
            max_v = sum_j  # 최대 합 갱신

    # 대각선 합 계산
    sum_main_diag = 0  # 정방향 대각선의 합을 0으로 설정
    sum_anti_diag = 0  # 역방향 대각선의 합을 0으로 설정

    for i in range(100):  # 행 순회
        sum_main_diag += arr[i][i]  # 정방향 대각선의 합 계산
        sum_anti_diag += arr[i][99-i]  # 역방향 대각선의 합 계산 (100 - 1 -i)

    if sum_main_diag > max_v:  # 현재 정방향 대각선의 합이 최대 합보다 크다면
        max_v = sum_main_diag  # 최대 합 갱신
        
    if sum_anti_diag > max_v:  # 현재 역방향 대각선의 합이 최대 합보다 크다면
        max_v = sum_anti_diag  # 최대 합 갱신

    print(f'#{tc_n} {max_v}')  # 결과 출력