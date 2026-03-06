import sys
sys.stdin = open('input.txt')


# 16진수를 2진수로 변환하는 함수
def hex_to_binary(hex_str):
    binary_str = ""  # 변환된 2진수 문자열을 담을 변수
    for char in hex_str:  # 16진수 문자열을 순회
        # 각 16진수 문자를 10진수로 변환 후 2진수 문자열로 변환
        # bin() 함수는 '0b' 접두사를 붙임 -> [2:]를 이용해 제거
        binary_num = bin(int(char, 16))[2:]
        binary_str += binary_num.zfill(4)  # 2진수 문자열의 자리를 4로 맞추기
    return binary_str


# 2진수를 10진수로 변환하는 함수
def binary_to_decimal(binary_str):
    decimal_num = 0  # 10진수 값을 저장할 변수
    pow = 0  # 지수

    for digit in reversed(binary_str):  # 2진수 문자열을 뒤집어서 순회
        if digit == '1':  # 현재 문자가 1이면
            decimal_num += 2 ** pow  # 2의 현재 지수만큼 곱한 값을 더하기
        pow += 1  # 지수 1 증가

    return decimal_num


T = int(input())
for tc in range(1, T+1):
    hexadecimals = input()  # 16진수 문자열 입력
    final_binary = hex_to_binary(hexadecimals)  # 16진수 문자열을 2진수 문자열로 변환

    print(f'#{tc}', end=' ')  # 테스트 케이스 번호 출력
    for i in range(0, len(final_binary), 7):  # 7비트씩 잘라서 순회
        # 현재 구간을 7비트 길이로 슬라이싱
        # 문자열의 끝을 넘지 않도록 길이 제한
        curr = final_binary[i:min(i + 7, len(final_binary))]
        result = binary_to_decimal(curr)  # 7비트 2진수 문자열을 10진수로 변환
        print(result, end=' ')  # 결과 출력
    print()  # 다음 테스트 케이스를 위한 줄바꿈