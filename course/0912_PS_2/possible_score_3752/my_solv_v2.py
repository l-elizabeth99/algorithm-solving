import sys
sys.stdin = open('sample_input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 문제 수
    score_lst = list(map(int, input().split()))  # N개의 배점 리스트
    max_score = sum(score_lst)  # 가능한 최대 점수 계산

    # 가능한 점수를 저장할 배열
    possible_score = [False] * (max_score + 1)
    possible_score[0] = True  # 0점은 가능

    # 문제의 배점을 순회
    for p_score in score_lst:
        # 최대 점수부터 역순으로 순회
        for score in range(max_score, -1, -1):
            # 현재 점수가 가능한 점수에 있으면 현재 점수+배점도 가능하다고 설정
            if possible_score[score]:
                possible_score[score + p_score] = True

    print(f'#{tc}', possible_score.count(True))  # 가능한 점수의 개수 출력