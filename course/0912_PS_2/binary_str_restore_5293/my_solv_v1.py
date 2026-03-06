import sys
sys.stdin = open('sample_input.txt')


def find_binary_str(fist, seceond, third, fourth):
    # 01, 10의 개수가 둘 다 없으면 00이나 11 중에 적어도 하나는 1개 이상이어야 함
    if seceond == 0 and third == 0:
        # 00과 11이 둘 다 있으면 불가능
        if fist > 0 and fourth > 0:
            return 'impossible'

        # 00이 1개 이상이면 00의 개수+1만큼 0으로 채우기
        if fist > 0:
            return '0' * (fist + 1)

        # 11이 1개 이상이면 11의 개수+1만큼 1로 채우기
        if fourth > 0:
            return '1' * (fourth + 1)

    # 01과 10의 차이가 2이상인 경우는 불가능
    if abs(seceond - third) > 1:
        return 'impossible'

    # 결과를 담을 리스트
    result = []

    # 01이 10보다 크다면
    if seceond > third:
        # 00의 개수+1만큼 0으로 채운 후
        result.append('0' * (fist+1))
        # 1과 0을 둘 중 작은 수(10의 개수)만큼 채우고
        for _ in range(third):
            result.append('10')
        # 11의 개수+1만큼 1로 채우기
        result.append('1' * (fourth+1))

    # 01이 10보다 작다면
    elif seceond < third:
        # 11의 개수+1만큼 1로 채운 후
        result.append('1' * (fourth+1))
        # 0과 1을 둘 중 작은 수(01의 개수)만큼 채우고
        for _ in range(seceond):
            result.append('01')
        # 00의 개수+1만큼 0으로 채우기
        result.append('0' * (fist+1))

    # 01과 10의 개수가 같다면
    elif seceond == third:
        # 00의 개수+1만큼 0으로 채운 후
        result.append('0' * (fist+1))
        # 1과 0을 01과 10의 개수만큼 채우고
        for _ in range(seceond):
            result.append('10')
        # 11의 개수+1만큼 1로 채우기
        result.append('1' * (fourth+1))

    # 결과를 하나로 묶기
    return ''.join(result)


T = int(input())
for tc in range(1, T+1):
    A, B, C, D = map(int, input().split())
    result_str = find_binary_str(A, B, C, D)  # 함수 호출한 결과를 결과 문자에 할당
    print(f'#{tc}', result_str)  # 결과 문자 출력