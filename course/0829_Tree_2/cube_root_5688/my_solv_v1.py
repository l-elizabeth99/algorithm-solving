import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 정수
    X_float = N**(1/3)  # 정수의 세제곱근을 계산
    X = int(round(X_float))  # 세제곱근을 부동소수점에 가까운 정수로 계산
    if X**3 == N:  # 계산한 값이 정수이면 그 값을 출력
        print(f'#{tc}', X)
    else:  # 아니면 -1을 출력
        print(f'#{tc}', -1)