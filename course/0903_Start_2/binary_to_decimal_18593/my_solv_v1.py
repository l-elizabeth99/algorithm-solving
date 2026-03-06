import sys
sys.stdin = open('input.txt')


# 2진수를 10진수로 변환하는 함수
def binary_to_decimal(binary_str):
    decimal_num = 0
    pow = 0

    for digit in reversed(binary_str):
        if digit == '1':
            decimal_num += 2 ** pow
        pow += 1

    return decimal_num


T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 입력 개수
    bit_arr = []  # 비트 배열을 담을 리스트
    for _ in range(N):  # N만큼 반복
        arr = input().strip()  # 배열 입력받기
        bit_arr.append(arr)  # 배열을 비트 배열에 담기
    bit_str = "".join(bit_arr)  # 비트 배열을 하나의 문자열로 지정
    print(f'#{tc}', end=' ')
    for i in range(0, len(bit_str), 7):  # 0부터 끝까지 7을 주기로 반복
        # i부터 i+7을 현재 구간으로 지정 - 구간이 7이 안되면 남은 길이만큼만
        curr = bit_str[i:min(i+7, len(bit_str))]
        result = binary_to_decimal(curr)  # 함수에 현재 구간을 넣은 것을 결과로 지정
        print(result, end=' ')  # 결과 출력