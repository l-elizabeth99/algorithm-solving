import sys
sys.stdin = open('input.txt')

T = int(input())  # 테스트 케이스 수

for tc in range(1, T+1):  # 테스트 케이스의 수만큼 반복
    N, M = map(int, input().split())  # NxN 배열과 MxM 배열의 수
    # 5 <= N <= 15
    # 2 <= M <= N
    # 한 영역의 파리 수 <= 30

    arr = [list(map(int, input().split())) for _ in range(N)]  # 2차원 배열에 저장

    max_flies = 0  # 최대 파리 개수를 0으로 설정

    # 전체 범위 중 파리채를 내리칠 수 있는 영역의 범위 = N - M + 1
    for i in range(N - M + 1):  # 범위의 행을 우선 순회
        for j in range(N - M + 1):  # 그 다음 범위의 열을 순회
            current_flies = 0  # 현재 영역의 파리 수를 0으로 설정

            # 현재 범위(파리채 영역)에서 파리가 존재하는 영역의 범위 : 각 열/행부터 M+열/행까지
            for p in range(i, M+i):  # 범위의 행을 우선 순회
                for q in range(j, M+j):  # 그 다음 범위의 열을 순회
                    current_flies += arr[p][q]  # 현재 영역의 파리 수를 더하기

            if current_flies > max_flies:  # 현재 파리 수가 최대 파리 수보다 크다면
                max_flies = current_flies  # 최대 파리 수를 갱신

    print(f'#{tc} {max_flies}')  # 결과 출력