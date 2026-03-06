import sys
sys.stdin = open('sample_input.txt')

T = int(input())  # 테스트 케이스 수
for tc in range(1, T+1):  # 테스트 케이스만큼 반복
    infix = input()  # 수식 문자열 받기
    stack = []  # 빈 스택 생성
    postfix = []  # 마지막 후위 배열을 담을 리스트

    icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}  # 연산자 우선순위 - 밖에 있을 때
    isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}  # 연산자 우선순위 - 안에 있을 때

    for i in infix:  # 수식 문자열만큼 반복
        if i.isdigit():  # 현재 문자가 숫자라면
            postfix.append(i)  # 새 리스트에 현재 문자 담기

        elif i == ')':  # 현재 문자가 닫는 괄호라면
            # 스택이 빌 때까지,
            # 스택의 마지막 문자가 여는 괄호가 될 때까지 반복
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())  # 새 리스트에 스택의 문자를 빼서 넣기

            if stack:  # 스택이 채워져 있다면
                stack.pop()  # 스택에서 빼기

        else:  # 현재 문자가 연산자라면
            # 스택이 빌 때까지,
            # 스택의 마지막 문자가 여는 괄호가 될 때까지 반복
            while stack and isp[stack[-1]] >= icp[i]:
                    postfix.append(stack.pop())  # 새 리스트에 스택의 문자를 빼서 넣기
            stack.append(i)  # 스택에 현재 문자 담기

    while stack:  # 스택이 빌 때까지 반복
        postfix.append(stack.pop())  # 새 리스트에 스택의 문자를 빼서 넣기

    print(f'#{tc}', ''.join(postfix))  # 결과 출력