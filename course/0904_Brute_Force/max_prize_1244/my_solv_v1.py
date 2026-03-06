import sys
sys.stdin = open('input.txt')


# 최대 금액을 찾는 함수
def find_max_prize(num, swap, max_swap, memo):
    # 상태를 튜플로 묶어 메모이제이션 키로 사용: 리스트는 가변이라 딕셔너리 키로 사용 못 함
    state = (tuple(num), swap)
    if state in memo:
        return memo[state]

    # 종료 조건: 교환 횟수가 최대 횟수면 정수로 변환해 반환
    if swap == max_swap:
        return int(''.join(map(str, num)))

    # 최댓값 지정, 숫자 길이 지정
    max_value = 0
    n = len(num)

    # 모든 숫자 교환 조합 탐색
    for i in range(n):
        for j in range(i+1, n):
            # 상태 변경: 숫자 위치 교환
            num[i], num[j] = num[j], num[i]

            # 재귀 호출, 최댓값 갱신
            result = find_max_prize(num, swap+1, max_swap, memo)
            max_value = max(max_value, result)

            # 상태 복원: 숫자 위치 교환
            num[i], num[j] = num[j], num[i]

    # 메모이제이션에 최댓값 지정
    memo[state] = max_value

    # 최댓값 반환
    return max_value


# 풀이 함수
def solve_prize_problem(str_num, max_swap):
    # 메모이제이션을 위한 딕셔너리 초기화
    memo = {}

    # 숫자를 리스트로 변환: 가변성 확보
    num = list(map(int, str_num))

    # 최대 금액을 찾는 함수를 호출해 반환
    return find_max_prize(num, 0, max_swap, memo)


T = int(input())
for tc in range(1, T+1):
    # 숫자판 정보, 교환 횟수
    num_str, max_changes_str = input().split()
    max_changes = int(max_changes_str)  # 교환 횟수를 정수로 변환
    memo = {}  # 메모이제이션을 위한 딕셔너리
    results = solve_prize_problem(num_str, max_changes)  # 풀이 함수 호출 및 결과에 할당
    print(f'#{tc}', results)  # 결과 출력