import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 전선 개수
    lines = []  # 전선의 위치를 담을 리스트
    for _ in range(N):  # 전선 개수만큼 반복
        start, end = map(int, input().split())  # 첫번째 위치, 두번째 위치
        lines.append((start, end))  # 리스트에 입력받은 위치들을 튜플로 넣기
    cross = 0  # 교차점의 수를 담을 변수
    for i in range(N):  # 처음부터 끝까지 반복
        for j in range(i+1, N):  # 앞의 수보다 하나 많은 수부터 끝까지 반복
            # 현재 전선의 위치를 리스트에서 꺼내서 따로 저장
            s1, e1 = lines[i]
            s2, e2 = lines[j]
            # 한 전선이 다른 전선보다 시작점이 낮고, 끝점이 높으면
            if (s1 < s2 and e1 > e2) or (s1 > s2 and e1 < e2):
                cross += 1  # 교차점 1 누적
    print(f'#{tc}', cross)  # 교차점 출력