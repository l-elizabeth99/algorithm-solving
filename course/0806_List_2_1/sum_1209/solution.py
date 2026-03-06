import sys
sys.stdin = open('input.txt')

'''
리스트의 크기 : 100 x 100
테스트 케이스의 깃수 : 10
각 행의 합, 각 열의 합, 각 대각선의 합 중에서 가장 큰 값

행의 합 구하기
-> 열의 합 구하기
-> 대각선의 합 구하기
-> 최댓값 찾기
'''

T = 10
N = 100  # 리스트의 크기
for tc in range(1, T+1):
    _ = input()  # 써도 되고 안 써도 됨 - tc와 역할이 겹침
                 # 안 써도 생략하면 input()이 꼬임
                 # _ : 입력은 받지만, 안 쓰는 경우

    # list comprehension이 익숙하지 않은 경우
    # arr = []
    # for _ in range(N):
    #     arr.append(list(map(int, input().split())))

    # list comprehension을 사용하는 경우
    # [리스트의 요소 for i in range(5)]
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 최댓값을 저장해놓을 변수
    max_v = 0

    # 행의 합
    for i in range(N):
        total_row = 0
        for j in range(N):
            total_row = arr[i][j]

        if total_row > max_v:
            max_v = total_row

    # 열의 합
    for j in range(N):
        total_col = 0
        for i in range(N):
            total_col = arr[i][j]

        if total_col > max_v:
            max_v = total_col

    # 좌상단에서 우하향으로 내려가는 대각선의 합
    total_diag = 0
    for i in range(N):
        total_diag += arr[i][i]

    if total_diag > max_v:
        max_v = total_diag

    # 우상단에서 좌하향으로 내려가는 대각선의 합
    total_diag = 0
    for i in range(N):
        total_diag += arr[i][N-1-i]

    if total_diag > max_v:
        max_v = total_diag

    print(f'#{tc} {max_v}')