import sys
sys.stdin = open('ex1_input.txt')

T = int(input())  # 테스트 케이스 수

for tc in range(1, T+1):  # 테스트 케이스를 반복
    N = int(input())  # 배열의 수 (NxN)
    arr = [list(map(int, input().split())) for _ in range(N)]  # 2차원 배열에 저장

    total_sum = 0  # 전체 합을 0으로 설정

    # 방향별로 더할 값 : 오른쪽부터 시계방향
    di = [0, 1, 0, -1]  # 행 기준
    dj = [1, 0, -1, 0]  # 열 기준

    for i in range(N):  # 배열 중 행을 먼저 순회
        for j in range(N):  # 배열 중 열을 순회
            for d in range(4):  # 4번(상하좌우) 반복
                ni, nj = i + di[d], j + dj[d]  # 행과 열에 각각 더하기

                if 0 <= ni < N and 0 <= nj < N:  # 상하좌우의 칸 수가 배열의 크기보다 작다면(유효한 인덱스라면)
                    total_sum += abs(arr[i][j] - arr[ni][nj])  # 차이값에 절댓값 씌우기

    print(f'#{tc} {total_sum}')  # 결과 출력