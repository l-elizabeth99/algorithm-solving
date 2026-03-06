import sys
sys.stdin = open('sample_input.txt')

T = int(input())  # 테스트 케이스 수

for tc in range(1, T+1):  # 테스트 케이스만큼 반복
    N = int(input())  # 칠할 영역의 개수

    grid = [[0] * 10 for _ in range(10)]  # 0으로 채워진 10x10 격자 생성

    # 색칠하기
    for _ in range(N):  # 칠할 영역의 개수만큼 반복

        # 왼쪽 위 인덱스와 오른쪽 아래 인덱스와 색상 정보
        r1, c1, r2, c2, colour = map(int, input().split())

        # 행부터 순회하며 해당 인덱스에 숫자 붙이기(색칠하기)
        for r in range(r1, r2 + 1):  # 행 먼저 순회
            for c in range(c1, c2 + 1):  # 열 순회

                # 3(보라색)이 아니면 색칠 - 빨강이면 1, 파랑이면 2
                if grid[r][c] != 3:  # 해당 영역이 3(보라색)이 아니면
                    grid[r][c] += colour  # 색상 정보를 더하기

    # 보라색 칸의 수 세기
    purple_count = 0  # 보라색 칸의 수를 0으로 설정

    # 행부터 순회하며 보라색 칸의 수 세기
    for r in range(10):  # 행 먼저 순회
        for c in range(10):  # 열 순회

            # 3(보라색)이면 세기
            if grid[r][c] == 3:  # 해당 칸이 3이면(보라색이면)
                purple_count += 1  # 보라색 칸의 수를 갱신

    print(f'#{tc} {purple_count}')  # 결과 출력