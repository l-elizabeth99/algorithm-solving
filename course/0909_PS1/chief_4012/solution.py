import sys
sys.stdin = open('sample_input.txt')

'''
재료 : N개
음식별 재료 : N//2 - 조합 사용
    - 재료를 뽑는 순서 : 상관 x => 순열 x, 조합 o
    
음식 재료의 절반 중 2개씩 요리
    - 재료를 뽑는 순서 : 상관 x => 순열 x, 조합 o
    - 해당 재료를 뽑아 요리했을 때의 총합 구하기
    - A와 B의 차이 계산
    - 최솟값 찾기
'''

# goal : 뽑으려는 원소
# target : 뽑아야 하는 개수
# choice : 현재 뽑은 요소가 들어있는 리스트
# start : 뽑는 요소의 인덱스 정보 갱신
# [(1, 2), (1, 3), ... , (3, 4)] 로 반환


def combination(goal, target, choice, start):
    result = []  # combination의 반환 값

    # 종료 조건 : 뽑은 개수가 뽑아야 하는 개수와 같으면 종료
    if len(choice) == target:
        result.append(choice[:])  # choice의 메모리 주소가 복사 -> choice 변경시 result도 변경
        return result

    for idx in range(start, len(goal)):  # 뽑은 것을 다시 선택하지 않도록 범위 조정
        choice.append(goal[idx])  # 현재 값 선택
        result += combination(goal, target, choice, idx+1)  # idx의 다음 자리부터 다음 요소를 뽑으러 감
        choice.pop()  # 다른 선택을 위해 현재 선택된 값 제거

    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]

    # 최솟값 초기화
    min_value = float('inf')

    # 모든 재료에서 절반을 선택한 모든 조합
    ingregiant_a_lst = combination(list(range(N)), N//2, [], 0)

    # 조합 리스트에서 하나씩 조합을 꺼내 계산
    for ingregiant_a in ingregiant_a_lst:
        # b의 재료 : 모든 재료에서 a의 재료를 제외한 재료
        # ingregiant_b = [ingregiant for ingregiant in list(range(N)) if ingregiant not in ingregiant_a]
        ingregiant_b = list(set(range(N)) - set(ingregiant_a))

        # 뽑은 재료에서 2개씩 뽑아 요리
        synergy_a = 0
        for i, j in combination(ingregiant_a, 2, [], 0):
            synergy_a += S[i][j] + S[j][i]

        synergy_b = 0
        for i, j in combination(ingregiant_b, 2, [], 0):
            synergy_b += S[i][j] + S[j][i]

        min_value = min(min_value, abs(synergy_a-synergy_b))

    print(f'#{tc}', min_value)