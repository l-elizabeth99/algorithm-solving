import sys
sys.stdin = open('input.txt')

'''
암호코드 = 숫자 8개
숫자 1개 = 7개의 비트
-> 암호코드의 가로 길이 = 56

올바른 암호코드
(홀수 자리 합 x 3) + (짝수 자리 합) = 10의 배수
'''


# 받은 배열에서 암호코드 부분만 추출 - 가로 : 56, 세로 : 필요 없음
# 암호비트를 앞에서부터 7자리씩 끊기 : 총 8개


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # 세로 크기,가로 크기
    arr = [input() for _ in range(N)]  # N x M 배열 받기

    pw_bit = []  # 암호비트를 담을 리스트 생성
    is_pw = False  # 암호가 없다고 가정 : False
    for i in range(N-1, -1, -1):  # 행 먼저 순회
        for j in range(M-1, -1, -1):  # 열 순회 : 역순회
            if arr[i][j] == '1':  # 해당 자리의 값이 1인 경우
                # 암호비트 = 해당 행, 해당 열((해당 인덱스 -55) 부터 (해당 인덱스 + 1))
                pw_bit = arr[i][j-55:j+1]
                is_pw = True  # 암호가 있다고 설정 : True
                break
        if is_pw:  # 암호가 있으면
            break
    if not pw_bit:  # 암호비트가 없다면
        print(f'#{tc}', 0)  # 0을 출력

    # 암호 규칙을 딕셔너리로 저장
    patterns = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9,
    }
    pw = []  # 암호코드를 담을 리스트 생성
    for section in range(0, 56, 7):  # 0부터 56까지 7을 주기로 반복
        # 암호규칙의 현재부터 현재+7까지를 현재 구역으로 지정
        curr = pw_bit[section:section+7]
        # 암호코드에 현재 구역에 해당하는 암호규칙의 딕셔너리값을 넣기 - 암호규칙에 없는 코드면 -1을 지정
        pw.append(patterns.get(curr, -1))
    if -1 in pw:  # 암호코드에 -1이 있으면
        print(f'#{tc}', 0)  # 0을 출력

    odd_sum = 0  # 홀수의 합을 0으로 설정
    even_sum = 0  # 짝수의 합을 0으로 설정
    for idx in range(8):  # 8번 반복
        if idx % 2 == 0:  # 현재 인덱스를 2로 나눈 나머지가 0이면
            odd_sum += pw[idx]  # 홀수 합에 암호코드의 현재 인덱스 값을 더하기
        else:  # 현재 인덱스를 2로 나눈 나머지가 1이면
            even_sum += pw[idx]  # 짝수 합에 암호코드의 현재 인덱스 값을 더하기
    correct_sum = (odd_sum * 3) + even_sum  # 올바른 코드의 합을 (홀수 합 x 3) + (짝수 합)로 지정
    if correct_sum % 10 == 0:  # 올바른 코드의 합을 10으로 나눈 나머지가 0이면
        print(f'#{tc}', sum(pw))  # 암호코드의 합 출력
    else:  # 나머지가 0이 아니면
        print(f'#{tc}', 0)  # 0 출력