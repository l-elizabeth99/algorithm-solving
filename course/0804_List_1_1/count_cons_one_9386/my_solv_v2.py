import sys
sys.stdin = open('input1.txt')

T = int(input())  # 테스트 케이스 수
for tc in range(1, T+1):  # 테스트 케이스만큼 반복
    N = int(input())  # 수열의 길이
    arr = list(map(int, input()))  # 0과 1로 구성된 수열 - 공백없이

    max_count = 0  # 최대값을 0으로 설정
    count_1 = 0  # 연속한 1의 수를 0으로 설정
    for i in range(N):  # 수열의 길이만큼 반복
        if arr[i] == 1:  # 현재 값이 1이라면
            count_1 += 1  # 연속한 1의 수를 1 더함
        else:  # 현재 값이 0이라면
            count_1 = 0  # 연속한 1의 수를 0으로 지정

        if count_1 > max_count:  # 연속한 1의 수가 최대값보다 크다면
            max_count = count_1  # 최대값 갱신

    print(f'#{tc}', max_count)  # 결과 출력