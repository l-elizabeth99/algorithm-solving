import sys
sys.stdin = open('sample_input.txt')


def find_case_num(cnt, curr_score, possible_score):
    # 종료 조건: 모든 문제를 확인하면 가능한 점수에 현재 점수를 넣고 종료
    if cnt == N:
        possible_score.add(curr_score)
        return

    # 현재 문제를 맞힌 경우
    find_case_num(cnt + 1, curr_score + score_lst[cnt], possible_score)

    # 현재 문제를 틀린 경우
    find_case_num(cnt + 1, curr_score, possible_score)


T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 문제 수
    score_lst = list(map(int, input().split()))  # N개의 배점 리스트
    possible_score_set = set()  # 가능한 점수를 담을 set
    find_case_num(0, 0, possible_score_set)  # 함수 호출
    print(f'#{tc}', len(possible_score_set))  # 가능한 점수의 길이 출력