import sys
sys.stdin = open('4866_input.txt')

T = int(input())  # 테스트 케이스 수
for tc in range(1, T+1):  # 테스트 케이스만큼 반복
    brackets = input()  # 문자열
    stack = [0] * 100  # 100만큼 0으로 채워진 스택 생성
    
    top = -1  # 처음 요소를 -1로 지정
    ans = 1  # 유효한지 판단(유효하다고 가정)

    # 옳은 괄호 조합을 딕셔너리로 설정
    right_bracket = {
        '(': ')',
        '{': '}',
    }
    
    for i in brackets:  # 문자열만큼 반복
        if i in right_bracket.keys():  # 현재 문자가 딕셔너리의 키라면
            top += 1  # 처음 요소를 1 증가
            stack[top] = i  # 스택의 top번째 요소를 현재 문자로 지정

        elif i in right_bracket.values():  # 현재 문자가 딕셔너리의 값이라면
            if top == -1:  # 처음 요소가 -1이라면
                ans = 0  # 유효하지 않음
                break

            elif i != right_bracket[stack[top]]:  # 현재 문자와 top위치의 문자가 대응되지 않으면
                ans = 0  # 유효하지 않음
                break

            else:  # 그 외의 경우라면
                top -= 1  # 처음 요소의 위치를 1 감소

    if top != -1:  # 처음 요소의 위치가 -1이 아니라면
        ans = 0  # 유효하지 않음

    print(f'#{tc}', ans)  # 결과 출력