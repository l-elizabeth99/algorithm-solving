import sys
sys.stdin = open('input.txt')

T = 10  # 테스트 케이스 수
for tc in range(1, T+1):  # 테스트 케이스만큼 반복
    N = int(input())  # 정점의 개수
    for _ in range(N):  # 정점의 수만큰 반복
        # 정점의 번호, 정점의 문자, 왼쪽 자식의 번호, 오른쪽 자식의 번호
        num, txt, left, right = list(input().split())
    print(num)