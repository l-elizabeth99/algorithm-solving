import sys
sys.stdin = open('input.txt')

T = int(input())  # 테스트 케이스 수
for t in range(1, T + 1):
    N = int(input())  # 양수의 개수
    num = list(map(int, input().split()))  # N개의 숫자를 리스트로 설정
    max_num = num[0]  # 초기값을 첫번째 값으로 설정
    min_num = num[0]  # 초기값을 첫번째 값으로 설정

    for n in num:
        if n > max_num:  # 현재값이 초기값보다 크면
            max_num = n  # max_num 갱신
        if n < min_num:  # 현재값이 초기값보다 작으면
            min_num = n  # min_num 갱신
    diff = max_num - min_num  # 갱신된 최종 최댓값과 최종 최솟값을 더함
    print(f'#{t} {diff}')