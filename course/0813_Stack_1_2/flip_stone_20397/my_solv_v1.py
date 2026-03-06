import sys
sys.stdin = open('sample_in.txt')

# 테스트 케이스 수
T = int(input())

# 테스트 케이스만큼 반복
for tc in range(1, T+1):
    # 돌의 수, 뒤집기 횟수
    N, M = map(int, input().split())
    # 돌의 초기 상태
    stone_status = list(map(int, input().split()))

    # 뒤집기 횟수만큼 반복
    for _ in range(M):
        # 중간 돌 인덱스, 마주보는 돌의 수
        i, j = map(int, input().split())

        # 마주보는 돌의 수만큼 반복
        for k in range(1, j+1):
            left = i - k  # 왼쪽 인덱스
            right = i + k  # 오른쪽 인덱스

            # 해당 위치가 범위를 벗어나면 중지
            if left < 1 or right > N:
                break

            # 양 끝의 돌의 색이 같다면 뒤집기
            if stone_status[left-1] == stone_status[right-1]:
                stone_status[left-1] = 1 - stone_status[left-1]
                stone_status[right-1] = 1 - stone_status[right-1]

    # 결과 출력
    print(f'#{tc}', *stone_status)