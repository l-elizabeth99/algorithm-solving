import sys
sys.stdin = open('4873_input.txt')

T = int(input())  # 테스트 케이스 수
for tc in range(1, T+1):  # 테스트 케이스만큼 반복
    words = list(input())  # 문자열
    stack = [0] * 10001  # 0이 10001만큼 채워진 스택 생성

    top = -1  # 맨 위 위치를 -1로 지정

    for word in words:  # 문자열만큼 반복
        # 스택이 비워져 있지 않고, 현재 문자가 맨 위 위치의 문자와 같다면
        if top != -1 and word == stack[top]:
            top -= 1  # 맨 위 위치를 1 감소
        else:  # 아니라면
            top += 1  # 맨 위 위치를 1 증가
            stack[top] = word  # 맨 위 위치의 문자를 현재 문자로 지정

    print(f'#{tc}', top+1)  # 결과 출력