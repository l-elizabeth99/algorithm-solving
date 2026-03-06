import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card_name = input().split()
    mid = (N+1) // 2  # 홀수일 때, 앞에 하나 더 많아야 함
    pre_card = card_name[:mid]  # 초반 카드를 지정
    post_card = card_name[mid:]  # 나중 카드를 지정
    q = list()  # 큐를 지정
    while pre_card:  # 초반 카드가 존재하지 않을 때까지 반복
        q.append(pre_card.pop(0))  # 초반 카드의 첫번째를 빼서 큐에 넣기
        q.append(post_card.pop(0))  # 나중 카드의 첫번째를 빼서 큐에 넣기
        if pre_card and not post_card:  # 초반 카드가 있고, 나중 카드가 없다면
            q.append(pre_card.pop(0))  # 초반 카드의 첫번째를 빼서 큐에 넣기
            break  # 즉시 종료
    print(f'#{tc}', *q)  # 결과 출력