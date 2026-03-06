import sys
sys.stdin = open('sample_input.txt')


def find_max_score(idx, curr_score, curr_cal):
    global max_score

    # 종료 조건: 모든 재료를 선택하면 최대 점수 갱신 후 종료
    if idx == N:
        max_score = max(max_score, curr_score)
        return

    # 현재 재료를 선택하는 경우
    # 현재 재료의 칼로리를 추가해도 칼로리 제한을 넘지 않을 때만 다음 함수 호출
    if curr_cal + ingrediants[idx][1] <= L:
        find_max_score(idx + 1, curr_score + ingrediants[idx][0], curr_cal + ingrediants[idx][1])

    # 현재 재료를 선택하지 않는 경우
    find_max_score(idx + 1, curr_score, curr_cal)


T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())  # 재료 개수, 제한 칼로리

    # 재료에 대한 맛 점수, 칼로리
    ingrediants = []
    for _ in range(N):
        T, K = map(int, input().split())
        ingrediants.append((T, K))

    # 최대 점수 초기화 및 함수 호출
    max_score = 0
    find_max_score(0, 0, 0)

    # 최대 점수 출력
    print(f'#{tc}', max_score)