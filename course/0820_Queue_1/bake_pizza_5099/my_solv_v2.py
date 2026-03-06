import sys
sys.stdin = open('5099_input.txt')

from collections import deque


def create_pizzas_info(num, cheese):
    pizzas_info = []
    for i in range(num):
        pizzas_info.append((i + 1, cheese[i]))
    return pizzas_info


def bake_pizzas(size, num, info):
    q = deque()
    for _ in range(size):
        q.append(info.pop(0))

    baked_pizza = size

    while len(q) > 1:
        pizza_num, cheese_amount = q.popleft()
        cheese_amount //= 2
        if cheese_amount != 0:
            q.append((pizza_num, cheese_amount))
        else:
            if baked_pizza < num:
                q.append(info.pop(0))
                baked_pizza += 1
    return q[0][0]


T = int(input())
for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    C = list(map(int, input().split()))

    pizza_info = create_pizzas_info(M, C)
    leftover_pizza_num = bake_pizzas(N, M, pizza_info)
    print(f'#{tc}', leftover_pizza_num)