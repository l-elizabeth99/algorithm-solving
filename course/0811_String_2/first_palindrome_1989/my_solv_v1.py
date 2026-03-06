import sys
sys.stdin = open('input.txt')

T = int(input())  # 테스트 케이스 수
for tc in range(1, T+1):
    txt = input()  # 단어를 테스트 케이스만큼 받기

    count_char = 0  # 텍스트 수를 0으로 설정
    for char in txt:  # 하나의 단어만큼 반복
        count_char += 1  # 텍스트 수를 1씩 누적

    is_palindrome = 1  # 회문이면 1을 기본값으로 설정
    for i in range(count_char // 2):  # 텍스트 수를 2로 나눈 몫만큼 반복
        if txt[i] != txt[count_char - 1 - i]:  # 현재 글자가 반대쪽 글자와 다르면
            is_palindrome = 0  # 회문 여부를 0으로 설정

    print(f'#{tc}', is_palindrome)  # 결과 출력