import sys
sys.stdin = open('input1.txt')

T = int(input())  # 테스트 케이스 수

for tc in range(1, T+1):  # 테스트 케이스의 수만큼 반복
    N = int(input())  # 수열의 길이
    num = list(map(int, input()))  # 공백없는 수열을 리스트화

    current_count = 0  # 현재 1의 수
    max_count = 0  # 1의 수 중 최댓값

    for n in num:  # 수열을 순회
        if n == 1:  # 수열의 수가 1이라면
            current_count += 1  # 현재 1의 수 갱신
        else:  # 수열의 수가 0이라면
            current_count = 0  # 현재 1의 수를 0으로

        if current_count > max_count:  # 현재 1의 수가 최댓값보다 크면
            max_count = current_count  # 최댓값을 현재 1의 수로 갱신

    print(f'#{tc} {max_count}')  # 최댓값 출력