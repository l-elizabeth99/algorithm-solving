import sys
sys.stdin = open('sample_input.txt')

# 백트래킹, BFS, 다익스트라 모두 가능

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}')