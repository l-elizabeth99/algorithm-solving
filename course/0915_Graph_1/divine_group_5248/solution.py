import sys
sys.stdin = open('sample_input.txt')


def find_leader(x):
    if x != leader[x]:
        leader[x] = find_leader(leader[x])
    return leader[x]


def union(x, y):
    root_x = find_leader(x)
    root_y = find_leader(y)

    if root_x < root_y:
        leader[root_y] = root_x
    else:
        leader[root_x] = root_y


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    result = 0

    leader = list(range(N+1))
    for i in range(M):
        x, y = data[i*2], data[i*2+1]
        union(x, y)

    for i in range(N+1):
        find_leader(i)

    leader = set(leader)
    result = len(leader)-1

    print(f'#{tc}', result)