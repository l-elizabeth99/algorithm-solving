import sys
sys.stdin = open('5189_input.txt')

# 최솟값을 찾는 재귀 함수
def find_min(curr, visited, cost, costs, n):
    global min_battery
    if cost >= min_battery: return
    if len(visited) == n:
        min_battery = min(min_battery, cost + costs[curr][0])
        return
    for next_loc in range(n):
        if next_loc in visited: continue
        find_min(next_loc, visited + [next_loc], cost + costs[curr][next_loc], costs, n)

# 메인 루프
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]
    min_battery = float('inf')
    find_min(0, [0], 0, costs, N)
    print(f'#{t}', min_battery)