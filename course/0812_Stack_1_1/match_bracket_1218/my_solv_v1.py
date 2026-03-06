import sys
sys.stdin = open('input.txt')

T = 10  # 테스트 케이스 수
for tc in range(1, T+1):  # 테스트 케이스만큼 반복
    tc_len = int(input())  # 테스트 케이스의 길이
    brackets = list(input())  # 괄호문자로 이루어진 문자열
    stack = [0] * tc_len  # 테스트 케이스의 길이만큼 0으로 채워진 스택 생성

    top = -1  # 제일 처음 요소를 -1로 지정
    ans = 1  # 유효성 여부를 1로 지정 (유효하다고 가정)

    for i in brackets:  # 문자열만큼 반복
        if i in ['(', '[', '{', '<']:  # 현재 문자가 여는 괄호라면
            top += 1  # 처음 요소를 1씩 더하고
            stack[top] = i  # 스택의 top 위치를 현재 문자로 갱신

        elif i in [')', ']', '}', '>']:  # 현재 문자가 닫는 괄호라면
            if top == -1:  # 처음요소가 제일 아래라면
                ans = 0  # 유효하지 않다고 두고
                break  # 즉시 반복 종료

            if i == ')' and stack[top] != '(':  # 현재 문자가 ) 이고, 스택의 처음 요소가 (가 아니라면
                ans = 0  # 유효하지 않다고 두고
                break  # 즉시 반복 종료
            elif i == ']' and stack[top] != '[':  # 현재 문자가 ] 이고, 스택의 처음 요소가 [가 아니라면
                ans = 0  # 유효하지 않다고 두고
                break  # 즉시 반복 종료
            elif i == '}' and stack[top] != '{':  # 현재 문자가 } 이고, 스택의 처음 요소가 {가 아니라면
                ans = 0  # 유효하지 않다고 두고
                break  # 즉시 반복 종료
            elif i == '>' and stack[top] != '<':  # 현재 문자가 > 이고, 스택의 처음 요소가 < 가 아니라면
                ans = 0  # 유효하지 않다고 두고
                break  # 즉시 반복 종료

            else:  # 위의 조건들이 아닌 다른 경우라면
                top -= 1  # 처음 요소를 1씩 빼기

    if top != -1:  # 반복 종료후에 처음 요소가 제일 처음이 아니라면
        ans = 0  # 유효하지 않다고 두기

    print(f'#{tc}', ans)  # 결과 출력