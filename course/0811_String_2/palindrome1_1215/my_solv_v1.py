import sys
sys.stdin = open('input.txt')

T = 10  # 테스트 케이스 수
for tc in range(1, T+1):  # 테스트 케이스만큼 반복
    N = int(input())  # 회문의 길이
    arr = [list(input()) for _ in range(8)]  # 8x8 글자판

    count_palindrome = 0  # 회문 개수를 0으로 설정

    # 가로 회문 확인
    for i in range(8):  # 행 먼저 순회
        for j in range(8 - N + 1):  # 배열의 수에서  회문의 길이를 뺀만큼 반복 - 열 순회
            curr_palindrome = ''  # 회문 글자를 담을 빈 문자열 생성
            for k in range(N):  # 회문 길이만큼 반복
                curr_palindrome += arr[i][j + k]  # 문자열에 현재 글자 누적

            if curr_palindrome == curr_palindrome[::-1]:  # 현재 글자와 회문된 글자가 같으면
                count_palindrome += 1  # 회문 개수 1씩 누적

    # 세로 회문 확인
    for j in range(8):  # 열 먼저 순회
        for i in range(8 - N + 1):  # 배열의 수에서  회문의 길이를 뺀만큼 반복 - 행 순회
            curr_palindrome = ''  # 회문 글자를 담을 빈 문자열 생성
            for k in range(N):  # 회문 길이만큼 반복
                curr_palindrome += arr[i+k][j]  # 문자열에 현재 글자 누적

            if curr_palindrome == curr_palindrome[::-1]:  # 현재 글자와 회문된 글자가 같으면
                count_palindrome += 1  # 회문 개수 1씩 누적

    print(f'#{tc}', count_palindrome)