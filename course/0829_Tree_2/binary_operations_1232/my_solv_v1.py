import sys
sys.stdin = open('input.txt')


def post_order_calc(node):  # 후위 순회 계산 함수
    operation = ['+', '-', '*', '/']  # 연산자 정보
    node_value = par[node]  # 부모 노드의 값을 지정

    if node_value in operation:  # 값이 연산자에 있으면
        left_value = post_order_calc(left[node])  # 왼쪽 탐색한 결과를 왼쪽 값으로 지정
        right_value = post_order_calc(right[node])  # 오른쪽 탐색한 결과를 오른쪽 값으로 지정

        # 노드값의 연산자에 따라 계산한 값을 반환
        if node_value == '+':
            return left_value + right_value
        elif node_value == '-':
            return left_value - right_value
        elif node_value == '*':
            return left_value * right_value
        elif node_value == '/':
            return left_value / right_value

    else:  # 노드값이 연산자에 없으면 값을 정수로 반환
        return int(node_value)


T = 10
for tc in range(1, T+1):
    N = int(input())  # 정점의 수
    par = [0] * (N+1)  # 부모 정보
    left = [0] * (N+1)  # 왼쪽 자식 정보
    right = [0] * (N+1)  # 오른쪽 자식 정보

    for _ in range(N):
        node_info = list(map(str, input().split()))  # 정점의 정보
        node_num = int(node_info[0])  # 정점의 정보의 첫번째를 정점의 번호로 지정
        par[node_num] = node_info[1]  # 부모로 지정

        if len(node_info) > 2:  # 정점 정보의 길이가 2 초과이면
            left[node_num] = int(node_info[2])  # 왼쪽 자식으로 지정
            right[node_num] = int(node_info[3])  # 오른쪽 자식으로 지정

    result = int(post_order_calc(1))  # 노드를 1로 한 함수를 정수로 호출
    print(f'#{tc}', result)  # 결과 출력