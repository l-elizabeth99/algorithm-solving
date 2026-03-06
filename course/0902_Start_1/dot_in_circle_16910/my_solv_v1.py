import sys
sys.stdin = open('sample_input.txt')

T = int(input())  # 테스트 케이스
for tc in range(1, T+1):  # 테스트 케이스만큼 반복
    N = int(input())  # 반지름
    count = 0  # 격자점 개수를 세기 위한 것
    for x in range(-N, N+1):  # x의 범위만큼 반복
        for y in range(-N, N+1):  # y의 범위만큼 반복
            if x * x + y * y <= N * N:  # x^2 + y^2 <= N^2 이면
                count += 1  # 개수 세기
    print(f'#{tc}', count)  # 개수 출력