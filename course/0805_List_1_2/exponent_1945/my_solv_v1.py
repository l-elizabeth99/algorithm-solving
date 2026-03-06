import sys
sys.stdin =open('input.txt')

T = int(input())  # 테스트 케이스 수
for tc in range(1, T+1):  # 테스트 케이스만큼 반복
    N = int(input())  # 나눌 숫자
    primes = [2, 3, 5, 7, 11]  # 밑 리스트
    counts = [0] * 5  # 지수 개수

    for exp in range(5):  # 밑 만큼 반복
        p = primes[exp]  # 밑의 값을 새로 지정
        while N % p == 0:  # 숫자가 밑으로 나누어지지 않을 때까지 반복
            counts[exp] += 1  # 지수 개수 누적
            N //= p  # 숫자를 밑으로 나눈 몫으로 갱신

    print(f'#{tc}', *counts)  # 결과 출력