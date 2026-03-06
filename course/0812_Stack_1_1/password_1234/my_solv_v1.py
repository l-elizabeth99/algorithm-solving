import sys
sys.stdin = open('input.txt')

T = 10  # 테스트 케이스 수
for tc in range(1, T+1):  # 테스트 케이스만큼 반복
    info = input().split()  # 문자열 길이, 문자열을 모두 받기
    N = int(info[0])  # 문자열의 길이는 info의 0번째 인덱스의 정수값
    arr = info[1]  # 문자열은 info의 1번째 인덱스

    stack = [0] * N  # 문자열의 길이만큼 0으로 채워진 스택 생성

    top = -1  # 맨 위 위치를 -1로 지정
    for num in arr:  # 문자열을 순회
        # 맨 위 위치가 -1이 아니고(스택이 채워져 있고), 현재 문자가 맨 위 위치의 문자와 같다면
        if top != -1 and num == stack[top]:
            top -= 1  # 맨 위 위치를 1 감소
        else:  # 아니라면
            top += 1  # 맨 위 위치를 1 증가
            stack[top] = num  # 맨 위 위치의 값을 현재 문자로 갱신

    passwords = ""  # 비밀번호를 담을 빈 문자열 생성
    for pw in range(top+1):  # 스택만큼 반복
        passwords += stack[pw]  # 문자열에 맨 위 위치에 해당하는 스택 누적

    print(f'#{tc}', passwords)  # 결과 출력