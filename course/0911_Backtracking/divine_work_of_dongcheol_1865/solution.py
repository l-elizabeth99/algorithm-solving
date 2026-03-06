import sys
sys.stdin = open('input.txt')

'''
직원 N명
일 N개

일의 효율 P
Pij : i번째 직원이 j번째 일을 할 때의 효율

모든 직원이 서로 다른 일을 맡아야 함
이때의 최대 효율이 나오는 경우를 구해야 함
중복없는 순열 코드 사용
'''


def permutation(person, pre_p):  # person: 직원 인덱스, pre_p: 이전까지의 효율
    global max_p

    # 가지치기
    # 현재 효율이 지금까지 나온 최대 효율보다 작다면 최종 계산 결과가 최대 효율보다 작게 나옴
    if pre_p <= max_p:
        return

    # 종료조건
    if person == N:
        if pre_p > max_p:
            max_p = pre_p
        return

    for j in range(N):  # 일 선택
        if not worked[j]:
            worked[j] = True
            permutation(person+1, pre_p * P[person][j] * 0.01)  # 다음 선택
            worked[j] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 직원 수, 일 개수
    P = [list(map(int, input().split())) for _ in range(N)]  # 일의 효율
    worked = [False] * N  # 중복 선택 배제를 위한 방문 처리 배열
    max_p = 0
    permutation(0, 1)  # 100% 확률로 시작
    print(f'#{tc} {max_p * 100:.06f}')