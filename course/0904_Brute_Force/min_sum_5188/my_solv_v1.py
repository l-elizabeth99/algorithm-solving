import sys
sys.stdin = open('5188_input.txt')


def find_min_sum(r, c, curr_sum):
    global min_sum

    # 현재 합 계산
    curr_sum += arr[r][c]

    # 가지치기
    if curr_sum >= min_sum:
        return

    # 종료조건 : 행이 끝 번호이고 열도 끝 번호면 최솟값 갱신 후 종료
    if r == (N-1) and c == (N-1):
        min_sum = min(curr_sum, min_sum)
        return

    # 아래쪽으로 이동
    if (r+1) < N:
        find_min_sum(r+1, c, curr_sum)

    # 오른쪽으로 이동
    if (c+1) < N:
        find_min_sum(r, c+1, curr_sum)


T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 칸 수
    arr = [list(map(int, input().split())) for _ in range(N)]  # N x N 배열
    min_sum = float('inf')  # 무한대로 지정
    find_min_sum(0, 0, 0)  # 함수 호출
    print(f'#{tc}', min_sum)  # 결과 출력
