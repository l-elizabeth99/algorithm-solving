import sys
sys.stdin = open('sample_input.txt')

# 손님A : N/2개 선택
# 해당 식재료 인덱스에 해당하는 시너지 값 더하기
# 손님B : 남은 N/2개 선택
# 해당 식재료 인덱스에 해당하는 시너지 값 더하기

# 찾은 시너지 합의 차이를 절댓값으로 구하기
# 최소 차이 값 갱신


def find_synergy(dish):
    # 시너지 합 초기화
    synergy_sum = 0

    # 음식 재료만큼 돌며 두 재료가 다르면 해당 시너지를 누적
    for i in range(len(dish)):
        for j in range(len(dish)):
            if i != j:
                synergy_sum += synergy_arr[dish[i]][dish[j]]
    return synergy_sum


def find_min_diff(cnt, start):
    global min_diff

    # 종료 조건 : 식재료의 반을 세면 끝
    if cnt == N//2:

        # B 음식을 빈 리스트로 두고
        # 전체를 돌면서 A 음식에 없는 재료면 B 음식에 넣기
        B_dishes = []
        for i in range(N):
            if i not in A_dishes:
                B_dishes.append(i)

        # A, B 시너지 차 계산 (함수 호출로 계산) 및 최솟값과 비교 후 최솟값 갱신
        A_synergy = find_synergy(A_dishes)
        B_synergy = find_synergy(B_dishes)
        diff = abs(A_synergy - B_synergy)
        if diff < min_diff:
            min_diff = diff

        return

    # 현재부터 끝까지 돌며 현재 재료를 A에 넣고 재귀 호출 후 빼기
    for i in range(start, N):
        A_dishes.append(i)
        find_min_diff(cnt+1, i+1)
        A_dishes.pop()


T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 식재료 수
    synergy_arr = [list(map(int, input().split())) for _ in range(N)]  # NxN 배열의 시너지 값
    A_dishes = []  # A 재료를 담을 리스트
    min_diff = float('inf')  # 최소 차이
    find_min_diff(0, 0)  # 함수 호출

    print(f'#{tc}', min_diff)  # 최소 차이 출력