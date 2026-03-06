import sys
sys.stdin = open('input.txt')

T = int(input())  # 테스트 케이스 수
for tc in range(1, T+1):  # 테스트 케이스만큼 반복
    N = int(input())  # 카드 장 수
    arr = list(map(int, input()))  # N개의 숫자
    
    cards = [0] * 10  # 0으로 구성된 배열 생성

    for a in range(N):  # N번 반복
        cards[arr[a]] += 1  # 배열의 a번째에 1을 더함

    max_num = 0  # 가장 많이 적힌 숫자
    count_max = 0  # 가장 많이 적힌 숫자의 장 수
    for i in range(9, -1, -1):  # 끝에서부터 처음까지(역순으로) 반복
        if cards[i] > count_max:  # 배열의 i번째가 가장 많이 적힌 숫자의 장 수보다 크다면
            max_num = i  # 가장 많이 적힌 숫자를 i로 갱신
            count_max = cards[i]  # 가장 많이 적힌 숫자를 배열의 i번째로 갱신

    print(f'#{tc}', max_num, count_max)  # 결과 출력