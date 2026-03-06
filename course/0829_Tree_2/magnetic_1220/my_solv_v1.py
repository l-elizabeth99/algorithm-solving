import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    size = int(input())  # 테이블의 크기
    table = [list(map(int, input().split())) for _ in range(size)]  # 100x100 격자 배열
    # 1 : N극, 2 : S극
    # 테이블의 윗부분 - N
    # 테이블의 아랫부분 - S

    deadlock = 0  # 교착의 수를 세기 위한 것
    for j in range(size):  # 열 먼저 순회
        is_N = False  # N극의 존재 여부를 판단하기 위한 것
        for i in range(size):  # 행 순회
            if table[i][j] == 1:  # 현재 위치가 1일 경우
                is_N = True  # N극이 존재한다고 표시
            if table[i][j] == 2:  # 현재 위치가 2일 경우
                if is_N:  # N극이 존재하면
                    deadlock += 1  # 교착의 수를 누적
                    is_N = False  # N극이 존재하지 않는다고 표시
    print(f'#{tc}', deadlock)  # 결과 출력