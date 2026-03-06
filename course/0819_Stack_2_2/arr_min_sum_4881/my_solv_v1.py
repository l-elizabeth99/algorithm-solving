import sys
sys.stdin = open('4881_input.txt')


def min_sum_function(i, N, s):
    if i == N:
        print(p)
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]
            min_sum_function(i+1, N)
            p[i], p[j] = p[j], p[i]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    p = [i for i in range(N)]

    # print(arr, p)

    min_sum_function(0, N)