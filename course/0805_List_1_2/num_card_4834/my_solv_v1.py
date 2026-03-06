import sys
sys.stdin = open('input.txt')

T = int(input())  # 테스트 케이스 수

for tc in range(1, T + 1):  # 테스트 케이스 수만큼 반복
    N = int(input())  # 카드 장 수
    cards = list(map(int, input()))  # 카드 정보

    counts = [0] * 10  # 크기가 10인 배열 생성

    for card in cards:  # 모든 카드를 순회
        counts[card] += 1  # 카드의 숫자를 갱신

    max_num = 0  # 최대 숫자를 0으로 지정
    max_count = 0  # 최대 숫자의 개수를 0으로 지정

    for i in range(9, -1, -1):  # 인덱스 9부터 0까지 순회
        if counts[i] > max_count:  # 현재 숫자의 개수가 최대 숫자의 개수보다 크다면
            max_count = counts[i]  # 최대 숫자의 개수를 현재 숫자의 개수로 갱신
            max_num = i  # 최대 숫자를 현재 숫자로 갱신

    print(f'#{tc} {max_num} {max_count}')  # 최대 숫자와 최대 숫자의 개수 출력