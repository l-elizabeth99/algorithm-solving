import sys
sys.stdin = open('5099_input.txt')

from collections import deque

'''
테이스 케이스만큼 반복하며
    화덕의 크기와 피자의 개수를 입력받고
    피자에 뿌려진 치즈의 양을 리스트로 입력받기
    
    피자 정보(피자 번호와 치즈의 양)를 담을 리스트 생성
    피자의 수만큼 반복하며
        치즈 양의 인덱스+1과 값을 하나의 튜플로 묶어 피자 정보에 넣기
        
    화덕에 들어갈 큐를 생성
    화덕의 크기만큼 반복하며
        피자 정보의 값을 빼서 큐에 넣기
        
    화덕에 들어있고, 들어갔었던 피자의 수를 화덕의 크기로 지정

    피자의 수가 1이 될 때까지 반복
        큐에서 빼낸 튜플을 왼쪽부터 순서대로 피자 번호, 치즈의 양으로 지정
        치즈의 양을 반으로 줄이기
        
        치즈의 양이 0이 아니면
            해당 피자 정보를 다시 큐에 넣기

        치즈의 양이 0이면
            화덕을 거쳤던 피자의 수가 기존 피자의 수보다 작다면
                피자 정보에 남아있는 튜플을 큐에 넣고
                화덕을 거쳤던 피자의 수를 1 증가

    큐에 남아있는 피자의 번호 출력
'''

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    C = list(map(int, input().split()))

    pizza_info = []
    for i in range(M):
        pizza_info.append((i+1, C[i]))

    q = deque()
    for _ in range(N):
        q.append(pizza_info.pop(0))

    baked_pizza = N

    while len(q) > 1:
        pizza_num, cheese_amount = q.popleft()
        cheese_amount //= 2
        if cheese_amount != 0:
            q.append((pizza_num, cheese_amount))
        else:
            if baked_pizza < M:
                q.append(pizza_info.pop(0))
                baked_pizza += 1

    print(f'#{tc}', q[0][0])