import sys
sys.stdin = open('input.txt')


# 최대 금액을 찾는 재귀 함수
def find_max(num_list, swap, max_swap, memo):
    state = (tuple(num_list), swap)
    if state in memo: return memo[state]
    if swap == max_swap: return int(''.join(map(str, num_list)))

    max_val = 0
    n = len(num_list)
    for i in range(n):
        for j in range(i + 1, n):
            num_list[i], num_list[j] = num_list[j], num_list[i]
            max_val = max(max_val, find_max(num_list, swap + 1, max_swap, memo))
            num_list[i], num_list[j] = num_list[j], num_list[i]

    memo[state] = max_val
    return max_val


# 메인 루프
T = int(input())
for tc in range(1, T + 1):
    num_str, max_changes_str = input().split()
    max_changes = int(max_changes_str)
    num_list = list(map(int, num_str))
    memo = {}
    result = find_max(num_list, 0, max_changes, memo)
    print(f'#{tc}', result)